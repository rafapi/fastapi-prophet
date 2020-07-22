FROM python:3.7.8-slim-buster

RUN apt-get update \
  && apt-get -y install netcat build-essential postgresql \
  && apt-get clean

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./pre-reqs.txt .
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r pre-reqs.txt
RUN pip install -r requirements-dev.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
