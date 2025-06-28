FROM python:3.13.2-alpine3.21

WORKDIR /app

RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev

COPY herbiapi/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000