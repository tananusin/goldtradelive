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
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("price", 0))
        except Exception as e:
            st.error(f"❌ Error parsing gold price data: {e}")
    return 0

# Get USD to THB exchange rate
def get_usd_to_thb():
    url = f"https://financialmodelingprep.com/api/v3/fx/USDTHB?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("bid", 0))  # Use 'bid' as the price
            elif isinstance(data, dict):
                return float(data.get("bid", 0))  # Use 'bid' as the price
        except Exception as e:
            st.error(f"❌ Error parsing exchange rate data: {e}")
    return 0

# App title
st.title("💰 Gold Bar Cal.")

# Fetch live data
gold_price_oz_usd = get_gold_price()
usd_to_thb = get_usd_to_thb()

# Show fetched prices with optional manual override
st.subheader("📡 Live Market Data")
gold_price_oz_usd = st.number_input("Gold spot 99.99% 1 troy oz (USD)", value=gold_price_oz_usd, format="%.2f")
usd_to_thb = st.number_input("USD/THB exchange rate", value=usd_to_thb, format="%.2f")

# User Input: Budget
budget = st.number_input("Enter your budget in THB", value=0)

# Conversion constants
grams_per_oz = 31.1035

# Calculations
gold_price_per_oz_thb = gold_price_oz_usd * usd_to_thb if gold_price_oz_usd and usd_to_thb else 0
gold_price_per_gram_thb = gold_price_per_oz_thb / grams_per_oz if gold_price_per_oz_thb else 0

# Budget conversion
budget_per_oz = budget / gold_price_per_oz_thb if gold_price_per_oz_thb else 0
budget_per_gram = budget / gold_price_per_gram_thb if gold_price_per_gram_thb else 0

# Outputs
st.subheader("📊 Budget Breakdown")
st.write(f"**Budget:** {budget:,.0f} THB")
st.write(f"**99.99% gold:** {budget_per_oz:,.2f} troy oz")
st.write(f"**99.99% gold:** {budget_per_gram:,.2f} grams")

st.subheader("📈 Reference Prices")
st.write(f"Fetched Gold Price (USD/OZ): {gold_price_oz_usd}")
st.write(f"Fetched USD to THB Exchange Rate: {usd_to_thb}")
st.write(f"**1 troy oz of 99.99% gold =** {gold_price_per_oz_thb:,.0f} THB")
st.write(f"**1 gram of 99.99% gold =** {gold_price_per_gram_thb:,.0f} THB")
st.write(f"**1 kg LBMA 99.99% gold =** {gold_price_per_gram_thb*1000:,.0f} THB")
