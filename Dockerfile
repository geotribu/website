FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Build Directory
WORKDIR /tmp

# Install pip Requirements
ADD requirements.txt .

# Perform build and Cleanup Artifacts
RUN \
  apk add --no-cache \
    git \
    git-fast-import \
    openssh \
  && apk add --no-cache --virtual .build gcc musl-dev \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del .build gcc musl-dev \
  && rm -rf /tmp/*

# Set Working Directory
WORKDIR /App
