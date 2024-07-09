dockerfile_with_poetry = """FROM python:3.11.4-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

COPY ./backend/pyproject.toml ./
COPY ./backend/poetry.lock ./

RUN pip install --upgrade pip && pip install poetry
RUN poetry install

COPY ./backend ."""

dockerfile_without_poetry = """FROM python:3.11.4-slim-buster

WORKDIR /backend

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./backend ."""