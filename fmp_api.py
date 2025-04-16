# fmp_api.py (FMP - Financial Modeling Prep API provider)
import requests

def get_gold_price(api_key):
    url = f"https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("price", 0))
        except Exception as e:
            return f"❌ Error parsing gold price data: {e}"
    return 0

def get_usd_to_thb(api_key):
    url = f"https://financialmodelingprep.com/api/v3/fx/USDTHB?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("bid", 0))
            elif isinstance(data, dict):
                return float(data.get("bid", 0))
        except Exception as e:
            return f"❌ Error parsing exchange rate data: {e}"
    return 0