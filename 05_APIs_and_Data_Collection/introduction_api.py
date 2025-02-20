# Pandas is an API

import pandas as pd
import datetime
import plotly.graph_objects as go
from pycoingecko import CoinGeckoAPI

# Creating a dictrionary with data
dict = {'a': [11,21,31], 'b': [12,22,32]}
df = pd.DataFrame(dict)
print(type(df))
# Displaying the first few rows of the dataframe
print(df.head())
# Calculating the mean and returning the value
print(df.mean())

# REST APIs
# Using API called PyCoinGecko
# Using the get_coin_market_chart_by_id(id, vs_currency, days). 'id' is the name of the coin you want, 'vs_currency' is the currency you want the price in, and days is how many days back from today you want

cg = CoinGeckoAPI()
neoxa_data = cg.get_coin_market_chart_by_id(id='neoxa', vs_currency='brl', days=30)
print(type(neoxa_data))
neoxa_price_data = neoxa_data['prices']
print(neoxa_price_data[0:5])

# Turning the data into a Pandas DataFrame
data = pd.DataFrame(neoxa_price_data, columns=['TimeStamp', 'Price'])

# Now that we have the DataFrame we will convert the timestamp to datetime and save it as a column called Date. We will map our unix_to_datetime to each timestamp and convert it to a readable datetime
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms').dt.date

# Using this modified dataset we can now group by the Date and find the min, max, open, and close for the candlesticks
candlestick_data = data.groupby('Date', as_index=False).agg(
    Open=('Price', 'first'),
    High=('Price', 'max'),
    Low=('Price', 'min'),
    Close=('Price', 'last')
)

# Finally we are now ready to use plotly to create our Candlestick Chart.
fig = go.Figure(data=[go.Candlestick(
    x=candlestick_data['Date'],  # Axis X: date
    open=candlestick_data['Open'],   # Open price
    high=candlestick_data['High'],   # High price
    low=candlestick_data['Low'],     # Low price
    close=candlestick_data['Close']  # Close price
)])

fig.update_layout(title="Candlestick Graph - Neoxa (BRL)",
                  xaxis_title="Date",
                  yaxis_title="Price (BRL)",
                  xaxis_rangeslider_visible=False)

fig.write_html("candlestick_chart.html")