Here's an example `README.md` file for a Flask API hosted on GitHub:

# My Flask API

This is a simple Flask API that retrieves the value of the Unidad de Fomento (UF) for a given date. The UF is an index used in Chile to adjust prices, taxes, and other economic values. This API scrapes the UF value from the official website of the Servicio de Impuestos Internos (SII) in Chile.

## Usage

To use the API, send a GET request to the `/api/uf` endpoint with a `date` parameter in the format `YYYY-MM-DD`. For example, to retrieve the UF value for January 1, 2023, you would send the following request:

```
GET /api/uf?date=2023-01-01
```

The API will return a JSON object with the date and the value of the UF for that date:

```json
{
  "date": "2023-01-01",
  "value": 30679.06
}
```

If the requested date is invalid or outside the range of available data (January 1, 2013, to the present day), the API will return an error message and an appropriate status code.

## Installation

To run the API locally, you must have Python 3 and the required dependencies installed. You can install the dependencies using `pip` and the `requirements.txt` file:

```
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the API using the following command:

```
python app.py
```

The API will be available at `http://localhost:5000`.

## Testing

You can run tests using Pytest. Install Pytest using `pip`:

```
pip install pytest
```

Then, run the tests using the following command:

```
pytest
```

The tests are located in the `tests.py` file.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.