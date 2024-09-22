FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry && poetry install --no-root

COPY . /app

RUN poetry run pip install gunicorn

ENV APP_ROOT=/app
