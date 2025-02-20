FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . .
# COPY ../requirements.txt .
# COPY ../.env .

RUN pip install -r requirements.txt
RUN /bin/bash
