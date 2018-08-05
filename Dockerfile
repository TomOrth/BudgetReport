FROM ubuntu:latest
MAINTAINER Thomas Orth "torth212@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN mkdir -p /var/www/budgetreport
WORKDIR /var/www/budgetreport
ADD requirements.txt /var/www/budgetreport
RUN pip install -r requirements.txt
ADD . /var/www/budgetreport