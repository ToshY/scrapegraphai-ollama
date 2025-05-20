ARG PYTHON_IMAGE_VERSION=3.11

FROM python:${PYTHON_IMAGE_VERSION}-slim-bookworm AS base

LABEL maintainer="ToshY (github.com/ToshY)"

ENV PIP_ROOT_USER_ACTION=ignore
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /build

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade --force-reinstall 'setuptools>=65.5.1' \
    && python3 -m playwright install --with-deps chromium

FROM base AS dev

COPY --from=base /ms-playwright /ms-playwright

WORKDIR /app

COPY requirements.dev.txt ./

RUN pip install --no-cache-dir -r requirements.dev.txt