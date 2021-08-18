#pip install yfinance
import yfinance as yf

#pip install streamlit
import streamlit as st

import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#warnings.filterwarnings("ignore")

# Command prompt: streamlit run <file name>

# For st.write formatting refer to  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables 

st.write(""" 
         
# Stock Price App

Below are the stock **closing price** and ***volume*** of the stock of your choice:""") 

#st.write(tickerSymbol)


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
#tickerSymbol = 'GOOGL'



tickerSymbol = st.text_input('Input the Stock Symbol below to view price:', 'GOOGL')


#get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

start_d = st.text_input('Input start date yyyy-mm-dd:', '2021-01-01')

end_d = st.text_input('Input end date yyyy-mm-dd:', '2021-08-01')
                        

tickerDf = tickerData.history(period='1d', start = start_d, end= end_d)
#Open High Low Close VOlume Dividends Stock Splits

st.write("""
## Closing Price
          """)
          
st.line_chart(tickerDf.Close)

st.write(""" 
## Volume Price
         """)
st.line_chart(tickerDf.Volume)


