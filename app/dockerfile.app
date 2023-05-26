FROM ubuntu:focal 

WORKDIR /app

COPY ./requirements.txt .

RUN apt update -y
RUN apt upgrade -y

RUN apt install build-essential python3 -y
RUN apt install python-dev -y

RUN apt install python3-pip -y
RUN pip3 install wheel

RUN python3 -m pip install uwsgi

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 --version

RUN export PYTHONIOENCODING=utf8
RUN export LANG=en_US.UTF-8

COPY . .

RUN python3 manage.py collectstatic --noinput

