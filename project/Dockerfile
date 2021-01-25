###########
# BUILDER #
###########

FROM python:3.9.0-slim-buster as builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && apt-get clean

WORKDIR /usr/src/app

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip && pip install pip-tools
COPY ./pre-reqs.in .
COPY ./requirements.in .
COPY ./requirements-dev.in .
RUN pip-compile pre-reqs.in > pre-reqs.txt
RUN pip-compile requirements.in > requirements.txt
RUN pip-compile requirements-dev.in > requirements-dev.txt
RUN pip-sync pre-reqs.txt requirements.txt requirements-dev.txt
RUN pip install -r pre-reqs.txt
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.9.0-slim-buster

RUN apt-get update \
  && apt-get install -y --no-install-recommends postgresql netcat \
  && apt-get clean

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=builder /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY . .

RUN ls /opt/venv/bin

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
