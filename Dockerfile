FROM python:3.7-alpine

WORKDIR /usr/src/

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip pipenv

COPY src /usr/src/

COPY Pipfile /usr/src/

RUN pipenv install --skip-lock --system --dev