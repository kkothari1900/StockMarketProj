# Packages
import yfinance as yf
import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

#Collecting Google Stock price Data
today = date.today()
data_frame1 = today.strftime("%Y-%m-%d")
enddate = data_frame1
data_frame2 = date.today()-timedelta(days = 365)
data_frame2 = data_frame2.strftime("%Y-%m-%d")
startdate = data_frame2

#Downloading dataset from Google
data_google = yf.download('GOOG',start = startdate,end = enddate,progress=False)

# When Analyzing stock market, begin with candlestick chart. This chart will analyze the price movements of stock prices.
data_google["Date"] = data_google.index
data_google = data_google[["Date","Open","High","Low","Close","Adj Close","Volume"]]
data_google.reset_index(drop = True,inplace = True)
print(data_google.head())

# Now we visualize the candelstick chart of the Google Stock prices
figure1 = go.Figure(data_google =[go.Candlestick(x = data_google["Date"],open = data_google["Open"],high = data_google["High"],low = data_google["Low"],close = data_google["Close"])])
figure1.update_layout(title = "Google Stock Price Analysis",xaxis_rangeslider_visible = False)
figure1.show()