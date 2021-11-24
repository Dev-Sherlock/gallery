FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /gallery_service

WORKDIR /gallery_service

ADD . /gallery_service/

RUN pip install -r requirements.txt