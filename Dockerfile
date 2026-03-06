# == Builder Stage: Install dependencies with build tools ==
FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install build dependencies
RUN apk add --no-cache \
  gcc \
  musl-dev \
  libffi-dev \
  openssl-dev \
  cairo-dev \
  pango-dev \
  gdk-pixbuf-dev

# Copy and install Python dependencies
COPY requirements.txt ./
RUN python -m venv /opt/venv \
  && /opt/venv/bin/pip install --upgrade pip \
  && /opt/venv/bin/pip install -r requirements.txt


# == Runtime Stage: Minimal image for development ==

FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Geotribu Website Stack" \
  org.opencontainers.image.description="Technical stack to build Geotribu website." \
  org.opencontainers.image.source="https://github.com/geotribu/website/" \
  org.opencontainers.image.licenses="GPL-3.0-or-later"

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONOPTIMIZE=2 \
  LANG=fr_FR.UTF-8 \
  LANGUAGE=fr_FR:fr \
  LC_ALL=fr_FR.UTF-8 \
  PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies including French locale support
RUN apk add --no-cache \
  git \
  git-fast-import \
  openssh-client \
  libffi \
  musl-locales \
  musl-locales-lang \
  cairo \
  pango \
  gdk-pixbuf \
  && echo "export LANG=fr_FR.UTF-8" > /etc/profile.d/locale.sh

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application files for initial setup
COPY config/ ./config/
COPY hooks/ ./hooks/
COPY mkdocs.yml ./
COPY scripts/ ./scripts/

# Generate CLI help and merge config
RUN mkdir -p content/toc_nav_ignored/snippets/code \
  && geotribu --help > content/toc_nav_ignored/snippets/code/geotribu_cli_help.txt \
  && python scripts/100_mkdocs_config_merger.py -c mkdocs.yml

EXPOSE 8000

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
