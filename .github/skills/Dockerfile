# DAK Skill Library — Local Development Image
# Mirrors ghbuild.yml CI environment exactly.
# Base: hl7fhir/ig-publisher-base (Jekyll, Ruby, Java 17, Node.js)

FROM hl7fhir/ig-publisher-base:latest

LABEL org.opencontainers.image.title="DAK Skill Library"
LABEL org.opencontainers.image.source="https://github.com/WorldHealthOrganization/smart-base"

# Python packages — identical to ghbuild.yml
# --break-system-packages is required because the base image uses Debian's
# externally-managed Python; a venv is unnecessary inside a disposable container.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip python3-venv \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && pip3 install --break-system-packages \
        "GitPython>=3.1.40" \
        "PyYAML>=6.0" \
        "requests>=2.28.0" \
        "lxml" \
        "litellm>=1.0.0" \
        "pdfplumber" \
        "pandas" \
    && rm -rf /var/lib/apt/lists/*

# SUSHI — identical to ghbuild.yml
RUN npm install -g fsh-sushi

# IG Publisher jar — pre-baked so local runs don't need network
# Override: -v /local/publisher.jar:/app/publisher.jar
RUN mkdir -p /app/input-cache \
    && curl -L \
       https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar \
       -o /app/input-cache/publisher.jar

# DAK skill library
COPY . /app/skills/

# Workspace — mount IG repo here: -v $(pwd):/workspace
WORKDIR /workspace

ENV PUBLISHER_JAR=/app/input-cache/publisher.jar
ENV DAK_IG_ROOT=/workspace

ENTRYPOINT ["python3", "/app/skills/cli/dak_skill.py"]
CMD ["--help"]
