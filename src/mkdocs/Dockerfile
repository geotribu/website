# FROM python:3.7-slim-buster
FROM python:3.7-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade distrib
RUN apk add --no-cache \
    # dependencies for mkdocs-git-revision-date-localized-plugin
    git git-fast-import

# Install pip requirements
ADD src/mkdocs/requirements.txt .
RUN python -m pip install -r requirements.txt --no-cache-dir

WORKDIR /app
