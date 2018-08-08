FROM python:3.6.3
LABEL maintainer="torth212@gmail.com"

RUN mkdir -p /var/www/budgetreport
WORKDIR /var/www/budgetreport
ADD requirements.txt /var/www/budgetreport
RUN pip install -r requirements.txt
ADD . /var/www/budgetreport