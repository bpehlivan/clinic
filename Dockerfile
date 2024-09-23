FROM python:3.12.1-slim-bullseye

ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . ./app
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
