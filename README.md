# BudgetReport
[![image](https://travis-ci.org/TomOrth/BudgetReport.svg?branch=master)](https://travis-ci.org/TomOrth/BudgetReport)
Flask app to manage your budgets

## Running the program

1. Sign-up for AWS and create a postgres-based instace of the Relational Database Service
2. Take note of the database username, password, and endpoint URL
3. Install `docker` and `docker-compose`
4. Run the following command:
```bash
docker-compose run app -e RDS_USER=<value> -e RDS_PASSWRD=<value> -e RDS_HOST=<value>
```
and replace <value> with the appropriate value you got from AWS

## Running tests

1. Follow steps 1-3 from the above section but run this command instead:
```bash
docker-compose run test -e RDS_USER=<value> -e RDS_PASSWRD=<value> -e RDS_HOST=<value>
```

## Built With
* Python
* Flask
* Plotly.js
* AWS Relational Database Service (Postgres)
* AWS EC2 instance (Currently down to save AWS credit. Can be start upon request)
* JQuery
* jsPDF
* Docker

