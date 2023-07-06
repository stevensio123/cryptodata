from .coin_api_call_methods._1_get_asset import get_asset
from .coin_api_call_methods._2_get_asset_icons import get_asset_icons
from .coin_api_call_methods._3_get_exchange import get_exchange
from .coin_api_call_methods._4_get_exchange_icons import get_exchange_icons
from .coin_api_call_methods._5_get_symbols import get_symbols
from .coin_api_call_methods._6_get_exchange_rate import get_exchange_rate
from .coin_api_call_methods._7_get_exchange_rate_history import get_exchange_rate_history
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta


def asset_page_data_fetch(indv_asset_id, indv_exchange_id):
    # Defining fixed assets and exchange
    predefined_assets = ["BTC", "AUD", "LTC", "XRP", "NMC", "USDT", "DOGE", "ETH", "XLM", "BLZ", "DASH", "DAO", "SC", "LSK", "XMR", "AMP", "INDEX", "CUBE", "BAT", "ETC", "ARPA", "ZEC", "REP", "ATOM", "ZBC", "STX", "SCRT", "SUPER", "MDT", "WBTC", "AIR", "WAVES", "DOT", "INV", "FX", "GRT", "MLN", "QTUM", "LUNA", "COVAL", "GNO", "RLC", "ANT", "PLU", "ZEN", "SNT", "BNT", "OMG", "IOTA", "SAND", "CVC", "NMR",
                         "EOS", "XTZ", "KNC", "OCEAN", "STORJ", "NEO", "AVT", "MANA", "DNT", "BCH", "ZRX", "LRC", "TRX", "ICX", "LINK", "ADA", "REQ", "ENJ", "POWR", "TRIBE", "CTX", "QSP", "VET", "FIL", "DAI", "OXY", "MKR", "POLIS", "THETA", "GTC", "ZIL", "NANO", "TRAC", "REN", "ONT", "KIN", "ASTR", "LOOM", "CRPT", "NCT", "SHPING", "NKN", "IOTX", "FET", "XYO", "GUSD", "PAX", "MIR", "BCHSV", "AERGO", "CRV", "MUSD", "XRT", "FOX", "TLM", "BUSD"]
    predefined_exchanges = ["COINBASE", "BINANCE",
                            "BINANCEUS", "GEMINI", "KRAKEN"]

    # Fetching asset data
    asset = get_asset(indv_asset_id)

    # Fetching and updating asset icon
    asset_icons = get_asset_icons(12)
    asset_icon = next(
        (obj["url"] for obj in asset_icons if obj["asset_id"] == indv_asset_id), None)

    # Fetching exchange data
    exchange = get_exchange(indv_exchange_id)

    # Fetching and updating exchange icon
    exchange_icons = get_exchange_icons(12)
    exchange_icon = next(
        (obj["url"] for obj in exchange_icons if obj["exchange_id"] == indv_exchange_id), None)

    # Fetching symbol data
    symbols_raw = get_symbols("_USD", indv_exchange_id, indv_asset_id)
    symbols = [{'symbol_id': 'empty'}]
    if len(symbols_raw):
        symbols_processed = [symbol if symbol["symbol_type"] == "SPOT" and symbol["asset_id_quote"]
                             == "USD" else None for symbol in symbols_raw]
        symbols_processed = list(filter(None, symbols_processed))
        if len(symbols_processed):
            symbols = symbols_processed

    # Fetching exchange rates
    exchange_rates = get_exchange_rate(indv_asset_id)
    exchange_rates_list = []
    er_quote_asset_list = []
    if len(exchange_rates["rates"]):
        exchange_rates_list = exchange_rates["rates"]
        er_quote_asset_list = [rate["asset_id_quote"]
                               for rate in exchange_rates_list]

    # Fetching exchange rates history
    date_start_raw = datetime.utcnow() - timedelta(days=30)
    date_start = date_start_raw.isoformat()[:10]
    er_history = get_exchange_rate_history(
        indv_asset_id, "USD", "1DAY", date_start, 100)
    er_prices = []
    er_time_periods = []
    if len(er_history):
        er_prices = [rate["rate_close"] for rate in er_history]
        er_time_periods = [str((datetime.fromisoformat(
            rate["time_period_end"][:10])).strftime("%d-%B-%Y")) for rate in er_history]

    # Return data
    data = {"exchange": exchange[0], "asset": asset[0], "symbol": symbols[0], "exchange_rates": exchange_rates_list, "er_quote_asset_list": er_quote_asset_list, "er_prices": er_prices,
            "er_time_periods": er_time_periods, "asset_list": predefined_assets, "exchange_list": predefined_exchanges, "asset_icon_url": asset_icon, "exchange_icon_url": exchange_icon, "asset_id": indv_asset_id, "exchange_id": indv_exchange_id}
    return data


def crypto(request, indv_asset_id="BTC", indv_exchange_id="COINBASE"):
    try:
        context = asset_page_data_fetch(indv_asset_id, indv_exchange_id)
        return render(request, 'homepage.html', context=context)
    except Exception as e:
        return HttpResponse("Error:", e)


def homepage(request):
    return redirect('/crypto')
