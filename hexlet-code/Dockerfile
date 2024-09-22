FROM python:3.12

WORKDIR /app

# Сначала копируем только файлы зависимостей для установки
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем Poetry и зависимости
RUN pip install poetry && poetry install --no-root

# Затем копируем весь остальной код проекта
COPY . /app

# Устанавливаем gunicorn
RUN poetry run pip install gunicorn

ENV APP_ROOT=/app
