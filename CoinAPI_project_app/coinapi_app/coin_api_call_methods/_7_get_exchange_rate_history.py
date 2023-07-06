from requests import get
from json import loads
from .err_status import print_error_status
from .API_KEY import API_KEY


def get_exchange_rate_history(asset_id_base, asset_id_quote, period_id, time_start, limit):
    # Define the api endpoint url here
    api_url = f"https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history"

    # Assign the your API_KEY to authorization
    api_url_headers = {
        "authorization" : API_KEY,
    }

    # Define the api url parameters here
    api_url_parameters = {
        "period_id" : period_id, 
        "time_start" : time_start,
        "limit" : limit
    }

    # Making main API call
    res = get(url=api_url, headers=api_url_headers, params=api_url_parameters)

    # Returning an empty JSON object on failed requests
    if res.status_code != 200:
        print_error_status(res, "get_exchange_rate_history")
        return []
    else:
        parsed_json = loads(res.content)
        return parsed_json
