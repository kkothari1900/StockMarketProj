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

