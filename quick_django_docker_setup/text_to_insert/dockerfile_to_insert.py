def get_dockerfile_with_poetry(outer_foldername: str) -> str:
    return f"""FROM python:3.11.4-slim-buster

WORKDIR /{outer_foldername}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

COPY ./{outer_foldername}/pyproject.toml ./
COPY ./{outer_foldername}/poetry.lock ./

RUN pip install --upgrade pip && pip install poetry
RUN poetry install

COPY ./{outer_foldername} ."""


def get_dockerfile_without_poetry(outer_foldername: str) -> str:
    return f"""FROM python:3.11.4-slim-buster

WORKDIR /{outer_foldername}

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY .requirements.txt ./
RUN pip install -r requirements.txt

COPY ./{outer_foldername} ."""
