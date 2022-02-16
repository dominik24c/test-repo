FROM python:3.10.2-slim-buster

RUN apt-get update && \
    python3 -m pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN python3 -m pip install -r /requirements.txt

CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]