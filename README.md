# Stock Market predictions with Prophet and FastAPI

<p align="left">
   <img src="https://github.com/rafapi/fastapi-prophet/workflows/Continuous%20Integration/badge.svg?branch=master">
   <a href="https://github.com/rafapi/fastapi-prophet" target="_blank">
      <img src="https://codecov.io/gh/rafapi/fastapi-prophet/branch/master/graph/badge.svg" alt="Coverage">
   </a>
     <img src="https://img.shields.io/github/license/rafapi/fastapi-prophet">
     <img src="https://img.shields.io/github/last-commit/rafapi/fastapi-prophet">
</p>
The main objective of this project is to evaluate some async options for ML backends

## Details
* Dev stack
  * FastAPI: https://fastapi.tiangolo.com
  * SQLAlchemy: https://docs.sqlalchemy.org/en/14/core
  * Databases (Async SQLAlchemy Core access): https://github.com/encode/databases
  * fbprophet: https://facebook.github.io/prophet
  * yfinance: https://github.com/ranaroussi/yfinance
* Testing:
  * pytest: https://docs.pytest.org/en/stable
* Linting and Formatting:
  * black: https://github.com/psf/black
  * flake8: https://flake8.pycqa.org/en/latest
  * isort: https://pycqa.github.io/isort
* Continuous Integration via Github Actions

## Actions
* Train the model for a ticker
* Run a prediction for that ticker
* Fetch all the results or those of a specific ticker

## Future additions
* Authentication
* Extra information fields based on third-party content
* Add images if available from source
* Frontend for plots and human interaction
