/**
 * Fetch the pinned ci-health module into vendor/ and verify its sha256.
 *
 * The file is never committed here: the pin (commit + hash) is the record,
 * and a mismatch fails loudly rather than running unreviewed code.
 */
import { createHash } from "node:crypto";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import pin from "./pin.json" with { type: "json" };

const url = `https://raw.githubusercontent.com/${pin.repository}/${pin.ref}/${pin.path}`;
const res = await fetch(url);
if (!res.ok) {
  console.error(`fetch-pinned: ${url} returned HTTP ${res.status}`);
  process.exit(1);
}
const body = Buffer.from(await res.arrayBuffer());
const digest = createHash("sha256").update(body).digest("hex");
if (digest !== pin.sha256) {
  console.error(`fetch-pinned: sha256 mismatch for ${pin.path}\n  expected ${pin.sha256}\n  got      ${digest}`);
  process.exit(1);
}
const out = join(import.meta.dir, pin.into);
mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, body);
console.log(`fetch-pinned: ${pin.repository}@${pin.ref.slice(0, 7)}:${pin.path} -> ${pin.into} (sha256 ok)`);
