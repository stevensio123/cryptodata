from requests import get
from json import loads
from .err_status import print_error_status
from .API_KEY import API_KEY


def get_exchange(exchange_id):
    # Define the api endpoint url here
    api_url = f"https://rest.coinapi.io/v1/exchanges/{exchange_id}"

    # Assign the your API_KEY to authorization
    api_url_headers = {
        "authorization": API_KEY,
    }

    # Define the api url parameters here
    api_url_parameters = {
    }

    # Making main API call
    res = get(url=api_url, headers=api_url_headers, params=api_url_parameters)

    # Returning an empty JSON object on failed requests
    if res.status_code != 200:
        print_error_status(res, "get_exchange")
        return [{}]
    else:
        parsed_json = loads(res.content)
        if not len(parsed_json):
            return [{}]
        return parsed_json
