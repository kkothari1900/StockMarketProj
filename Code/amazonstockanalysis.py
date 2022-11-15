import yfinance as yf
import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt

#Collecting Google Stock price Data
today = date.today()
data_frame1 = today.strftime("%Y-%m-%d")
enddate = data_frame1
data_frame2 = date.today()-timedelta(days = 365)
data_frame2 = data_frame2.strftime("%Y-%m-%d")
startdate = data_frame2

#Downloading dataset from Amazon
data = yf.download('AMZN',start = startdate,end = enddate,progress=False)

# When Analyzing stock market, begin with candlestick chart. This chart will analyze the price movements of stock prices.
data["Date"] = data.index
data= data[["Date","Open","High","Low","Close","Adj Close","Volume"]]
data.reset_index(drop = True,inplace = True)
print(data.head())

# Now we visualize the candelstick chart of the Google Stock prices
figure = go.Figure(data =[go.Candlestick(x = data["Date"],
                                                open = data["Open"],
                                                high = data["High"],
                                                low = data["Low"],
                                               close = data["Close"])])
figure.update_layout(title = "Amazon Stock Price Analysis",xaxis_rangeslider_visible = False)
figure.show()
