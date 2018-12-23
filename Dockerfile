FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /not-holiday/
WORKDIR /not-holiday/
ADD requirements.txt /not-holiday/

RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install -y libpq-dev python-dev
RUN pip install psycopg2

# ADD projectile /code/docker