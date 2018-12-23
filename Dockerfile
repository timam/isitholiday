FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /not-holiday/
WORKDIR /not-holiday/
ADD requirements.txt /not-holiday/

RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install -y python3-mysqldb default-libmysqlclient-dev python-dev gdal-bin python3-gdal
RUN pip install mysqlclient

# ADD projectile /code/docker