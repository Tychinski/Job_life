# pull official base image
FROM python:3-slim as base

# set work directory
WORKDIR /app
COPY . .
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies


RUN apt-get update
RUN apt-get install bash

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project


# set the docker entry file
RUN chmod 777 /app/docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/docker-entrypoint.sh"]
