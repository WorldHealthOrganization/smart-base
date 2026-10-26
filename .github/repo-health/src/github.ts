/**
 * A minimal GitHub REST client. Any failure throws, and the caller turns
 * that into an `unknown` verdict: an unreadable answer is never treated as
 * an empty one.
 */

export class GitHubError extends Error {
  constructor(
    message: string,
    readonly status: number,
  ) {
    super(message);
  }
}

export interface GitHub {
  get<T>(path: string): Promise<T>;
  /** Follows `Link: rel="next"` up to `maxPages`. */
  list<T>(path: string, maxPages?: number): Promise<T[]>;
  send<T>(method: "POST" | "PATCH", path: string, body: unknown): Promise<T>;
  /** Count of requests made, for the run summary. */
  readonly calls: number;
}

export function github(token: string | undefined, base = "https://api.github.com"): GitHub {
  let calls = 0;
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "smart-repo-health",
  };
  if (token) headers.Authorization = `Bearer ${token}`;

  async function request(method: string, url: string, body?: unknown): Promise<Response> {
    calls++;
    const res = await fetch(url.startsWith("http") ? url : `${base}${url}`, {
      method,
      headers: body === undefined ? headers : { ...headers, "Content-Type": "application/json" },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    if (!res.ok) {
      const text = await res.text().catch(() => "");
      throw new GitHubError(`${method} ${url} -> HTTP ${res.status} ${text.slice(0, 200)}`, res.status);
    }
    return res;
  }

  return {
    get calls() {
      return calls;
    },
    async get<T>(path: string): Promise<T> {
      return (await request("GET", path)).json() as Promise<T>;
    },
    async list<T>(path: string, maxPages = 10): Promise<T[]> {
      const out: T[] = [];
      let next: string | undefined = path;
      for (let page = 0; next && page < maxPages; page++) {
        const res = await request("GET", next);
        const data = (await res.json()) as T[] | { workflow_runs?: T[]; workflows?: T[] };
        if (Array.isArray(data)) out.push(...data);
        else out.push(...((data.workflow_runs ?? data.workflows ?? []) as T[]));
        next = /<([^>]+)>;\s*rel="next"/.exec(res.headers.get("link") ?? "")?.[1];
      }
      return out;
    },
    async send<T>(method: "POST" | "PATCH", path: string, body: unknown): Promise<T> {
      return (await request(method, path, body)).json() as Promise<T>;
    },
  };
}
