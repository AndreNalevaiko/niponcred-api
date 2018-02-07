FROM python:3.5

MAINTAINER Andre Naleavaiko <andre@gorillascode.com>

RUN mkdir -p /niponcred-api/logs

WORKDIR /niponcred-api

RUN pip install -r requirements.txt

EXPOSE 5000