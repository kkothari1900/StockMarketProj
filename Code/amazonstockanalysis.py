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

# Creating a Bar plot: To analyze the stock: Amazon
figure = px.bar(data,x = "Date",y ="Close")
figure.show()


#Rangeslider helps analyze the stock price of Amazon between two specific points
figure = px.line(data, x ='Date',y='Close',
                title = 'AMAZON Stock Price Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible = True)
figure.show()

# Adding time period selectors: Buttons that show the graph of a specific time period (1 year, 3 months,6 months)
figure = px.line(data, x = 'Date', y ='Close',title = 'AMAZON Stock Price Analysis with Time Period Selectors')
figure.update_xaxes(
    rangeselector = dict(
        buttons = list([
            dict(count =1, label = "1m",step ="month",stepmode ="backward"),
            dict(count =6 , label ="6m",step ="month",stepmode ="backward"),
            dict(count =3, label = "3m",step ="month",stepmode ="backward"),
            dict(count =1, label = "1y",step ="year",stepmode ="backward"),
            dict(step="all")
        ])
    )
)
figure.show()
# This is how to remove all records of the weekend trends, this is because weekend or holiday weekend affects the stock market
figure = px.scatter(data, x = 'Date', y = 'Close',range_x = ['2021=07-12','2022-07-11'],title = "AMAZON Stock Price Analysis by Removing Weekend Gaps")
figure.update_xaxes(
    rangebreaks = [
        dict(bounds=["sat","sun"])
    ]
)
figure.show()
