FROM ubuntu:20.04

FROM python:3.8.3

RUN pip install flask

RUN pip install pandas

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
RUN wget https://datasets.imdbws.com/title.basics.tsv.gz
RUN gunzip title.basics.tsv.gz
COPY prepare.py /usr/src/app
RUN python prepare.py

COPY app.py /usr/src/app

RUN rm title.basics.tsv

ENTRYPOINT [ "python3", "app.py" ]