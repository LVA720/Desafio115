# syntax=docker/dockerfile:1.7

########################
# Builder
########################
FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim AS builder
WORKDIR /app

# Faster imports & stable file copies
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Copy metadata first for better caching
COPY pyproject.toml uv.lock* ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-install-project

# Now bring the source and do the project install
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked

########################
# Runner
########################
# Runner
FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim AS runner
WORKDIR /app

# Bring the project metadata so uv sees a project
COPY --from=builder /app/pyproject.toml /app/
COPY --from=builder /app/uv.lock* /app/

# Bring venv and source (editable install)
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src  /app/src
ENV PATH="/app/.venv/bin:${PATH}"

CMD ["uv", "run", "--no-sync", "python", "src/main.py"]
