Hide API key in streamlit
app setting -> secretes

[api_keys]
fmp_api_key = "actual api key"

----------------------------------------------------------------------

some fetch data has to be used as bid or ask, not always price

https://financialmodelingprep.com/api/v3/fx/USDTHB?apikey=actualapikey
[
  {
    "ticker": "USD/THB",
    "bid": 33.23,
    "ask": 33.367,
    "open": 33.52,
    "low": 33.3,
    "high": 33.531,
    "changes": -0.182,
    "date": "2025-04-15 22:55:44"
  }
]

https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey=actualapikey
[
  {
    "symbol": "XAUUSD",
    "name": "XAU/USD",
    "price": 3272.12,
    "changesPercentage": 1.3034,
    "change": 42.1,
    "dayLow": 3229.72,
    "dayHigh": 3275.42,
    "yearHigh": 3274.05,
    "yearLow": 2277.08,
    "marketCap": null,
    "priceAvg50": 2991.446,
    "priceAvg200": 2743.3684,
    "exchange": "FOREX",
    "volume": 105886,
    "avgVolume": 792706.2,
    "open": 3230.02,
    "previousClose": 3230.02,
    "eps": null,
    "pe": null,
    "earningsAnnouncement": null,
    "sharesOutstanding": null,
    "timestamp": 1744773088
  }
]