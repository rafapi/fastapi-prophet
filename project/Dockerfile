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
RUN pip install numpy==1.19.0 Cython==0.29.21 pandas==1.0.5 \
    LunarCalendar==0.0.9 holidays==0.10.2 convertdate==2.2.1 pystan==2.19.1.1
RUN pip install -r requirements.txt

# add app
COPY . .
