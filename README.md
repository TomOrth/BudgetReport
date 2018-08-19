# BudgetReport
[![image](https://travis-ci.org/TomOrth/BudgetReport.svg?branch=master)](https://travis-ci.org/TomOrth/BudgetReport) <br />
Flask app to manage your budgets

## Running the program

1. Sign-up for AWS and create a postgres-based instace of the Relational Database Service (RDS)
2. Create the environment variables `RDS_USER`, `RDS_PASSWRD`, and `RDS_HOST` with corresponding values from the RDS dashboard
3. Install `docker` and `docker-compose`
4. Run the following command:
```bash
sudo -E docker-compose -f docker-compose.yml up
```

## Running tests

1. Follow steps 1-3 from the above section but run this command instead:
```bash
sudo -E docker-compose -f docker-compose.test.yml up
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

