# Stock Market predictions with Prophet and FastAPI

![CI/CD](https://github.com/rafapi/fastapi-prophet/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

The main objective of this project is to evaluate some async options for ML backends

## Details
* Dev stack
  * FastAPI
  * SQLAlchemy[postgresql]
  * fbprophet
  * yfinance
* Testing: `pytest`
* Linting: `black`, `flake8` and `isort`
* CI/CD via Github Actions

## Actions
* Train the model for a ticker
* Run a prediction for that ticker
* Fetch all the results or those of a specific ticker

## ToDo
* Authentication
* Extra information fields based on third-party content
* Add images if available from source
