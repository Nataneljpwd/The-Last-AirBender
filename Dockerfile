FROM python:3.12-alpine

# Install poetry

RUN pip install poetry

#install and download dependencies

WORKDIR /app

COPY poetry.toml .
COPY pyproject.toml .

RUN python -m poetry install --no-root

# Copy rest of project

COPY . .
