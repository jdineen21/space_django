FROM python:3.8.0-buster

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000