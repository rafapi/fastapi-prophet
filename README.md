# Stock Market predictions with Prophet and FastAPI

![CI/CD](https://github.com/rafapi/fastapi-prophet/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

The main objective of this project is to evaluate some async options for ML backends

## Details
* CI via Github Actions
* Dev stack
  * FastAPI: https://fastapi.tiangolo.com
  * SQLAlchemy: https://docs.sqlalchemy.org/en/14/core
  * Databases (Async SQLAlchemy Core access): https://github.com/encode/databases
  * fbprophet: https://facebook.github.io/prophet
  * yfinance: https://github.com/ranaroussi/yfinance
* Testing:
  * pytest: https://docs.pytest.org/en/stable/
* Linting:
  * black: https://github.com/psf/black
  * flake8: https://flake8.pycqa.org/en/latest/
  * isort: https://pycqa.github.io/isort/

## Actions
* Train the model for a ticker
* Run a prediction for that ticker
* Fetch all the results or those of a specific ticker

## ToDo
* Authentication
* Extra information fields based on third-party content
* Add images if available from source
