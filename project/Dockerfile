FROM python:3.7.8-slim-buster

# install system dependencies
RUN apt-get update \
  && apt-get -y install build-essential \
  && apt-get clean

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./pre-reqs.txt .
RUN pip install -r pre-reqs.txt
RUN pip install -r requirements.txt

# add app
COPY . .
