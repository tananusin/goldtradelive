#Goldbartrading
import streamlit as st
import requests

# Set your API key
FMP_API_KEY = "VX427w8XiFyN3OBt20FxpzZjAr2MAoRu"

# Get live gold price (XAU/USD)
def get_gold_price():
    url = f"https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list):
            return data[0]["price"]
    return 0

# Get USD to THB exchange rate
def get_usd_to_thb():
    url = f"https://financialmodelingprep.com/api/v3/fx?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item["ticker"] == "USDTHB":
                return item["bid"]
    return 0

st.title("💰 Gold Bar Cal.")

# Fetch live data
gold_price_oz_usd = get_gold_price()
usd_to_thb = get_usd_to_thb()

# Show fetched prices (optional: allow editing)
st.subheader("📡 Live Market Data")
gold_price_oz_usd = st.number_input("Gold spot 99.99% 1 troy oz (USD)", value=gold_price_oz_usd)
usd_to_thb = st.number_input("USD/THB exchange rate", value=usd_to_thb)

# User Input: Budget
budget = st.number_input("Enter your budget in THB", value=0)

# Conversion constants
grams_per_oz = 31.1035

# Calculations
gold_price_per_oz_thb = gold_price_oz_usd * usd_to_thb
gold_price_per_gram_thb = gold_price_per_oz_thb / grams_per_oz

# Budget conversion
budget_per_oz = budget / gold_price_per_oz_thb if gold_price_per_oz_thb else 0
budget_per_gram = budget / gold_price_per_gram_thb if gold_price_per_gram_thb else 0

# Outputs
st.subheader("📊 Budget Breakdown")
st.write(f"**Budget:** {budget:,.0f} THB")
st.write(f"**99.99% gold:** {budget_per_oz:,.2f} troy oz")
st.write(f"**99.99% gold:** {budget_per_gram:,.2f} grams")

st.subheader("📈 Reference Prices")
st.write(f"**1 troy oz of 99.99% gold =** {gold_price_per_oz_thb:,.0f} THB")
st.write(f"**1 gram of 99.99% gold =** {gold_price_per_gram_thb:,.0f} THB")
st.write(f"**1 kg LBMA 99.99% gold =** {gold_price_per_gram_thb*1000:,.0f} THB")