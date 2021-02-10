# Stock Market predictions with Prophet and FastAPI

<p align="left">
   <img src="https://github.com/rafapi/fastapi-prophet/workflows/Continuous%20Integration/badge.svg?branch=master">
   <a href="https://github.com/rafapi/fastapi-prophet" target="_blank">
      <img src="https://codecov.io/gh/rafapi/fastapi-prophet/branch/master/graph/badge.svg" alt="Coverage">
   </a>
     <img src="https://img.shields.io/github/license/rafapi/fastapi-prophet">
     <img src="https://img.shields.io/github/last-commit/rafapi/fastapi-prophet">
</p>
Train prophet models and run stock market predictions for a given ticker

## Details
* Dev stack
  * FastAPI: https://fastapi.tiangolo.com
  * Docker: https://docs.docker.com/
  * SQLAlchemy: https://docs.sqlalchemy.org/en/14/core
  * Databases (Async SQLAlchemy Core queries): https://github.com/encode/databases
  * fbprophet (Time Series forecasting): https://facebook.github.io/prophet
  * yfinance: https://github.com/ranaroussi/yfinance
* Testing:
  * pytest: https://docs.pytest.org/en/stable
  * pytest-cov: https://github.com/pytest-dev/pytest-cov
  * Codecov: https://docs.codecov.io
* Linting and Formatting:
  * black: https://github.com/psf/black
  * flake8: https://flake8.pycqa.org/en/latest
  * isort: https://pycqa.github.io/isort
* Continuous Integration via Github Actions

## Actions
* Train the model for a ticker
### CRUD
   * Create prediction for that ticker
   * Read results for all tickers or for individual ones
   * Update the info for a ticker should be done by creating a new one since this date is only relevant for the given time input
   * Delete a specific ticker

## Future additions
* Authentication
* Extra information fields based on third-party content
* Add images if available from source
* Input training timeframe
* User Interface
