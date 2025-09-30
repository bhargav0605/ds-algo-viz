# ---------- 1) Builder: install deps into a venv ----------
FROM python:3.11-slim AS builder

# Faster/cleaner pip; no .pyc
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps for building wheels (add more if your deps need them)
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only dependency manifests first for better layer caching
# If you use pyproject.toml, replace the next two lines accordingly
COPY requirements.txt ./
RUN python -m venv /opt/venv \
 && . /opt/venv/bin/activate \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

# ---------- 2) Runtime: copy venv + app, run gunicorn ----------
FROM python:3.11-slim AS runtime

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Minimal runtime tools (curl used by HEALTHCHECK)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

# Non-root user
RUN useradd -m -u 10001 appuser

WORKDIR /app

# Bring in the prebuilt virtualenv
COPY --from=builder /opt/venv /opt/venv

# Now copy your application code
COPY . .

# Gunicorn tunables via env
ENV GUNICORN_APP="src.app:app" \
    GUNICORN_WORKERS="2" \
    GUNICORN_THREADS="8" \
    GUNICORN_TIMEOUT="60" \
    PORT="8000"

EXPOSE 8000

# Simple health endpoint: implement /health in your Flask app
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD curl -fsS "http://127.0.0.1:${PORT}/health" || exit 1

USER appuser

# Use exec form; logs to stdout/stderr
CMD ["sh", "-c", "exec gunicorn ${GUNICORN_APP} --bind 0.0.0.0:${PORT} --workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --timeout ${GUNICORN_TIMEOUT} --access-logfile - --error-logfile -"]
