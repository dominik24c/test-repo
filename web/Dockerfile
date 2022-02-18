FROM python:3.10.2-slim-buster

WORKDIR /app

RUN apt-get update

COPY ./requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

COPY . .




