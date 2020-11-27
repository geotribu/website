FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set build directory
WORKDIR /tmp

# Install pip requirements
ADD requirements.txt .

# Perform build and cleanup artifacts
RUN \
  apk add --no-cache \
    git \
    git-fast-import \
    openssh \
  && apk add --no-cache --virtual .build gcc musl-dev \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del .build gcc musl-dev \
  && rm -rf /tmp/*

# Set working directory
WORKDIR /app
