#pip install yfinance
import yfinance as yf

#pip install streamlit
import streamlit as st

# Command prompt: streamlit run <file name>

# For st.write formatting refer to  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables 

st.write(""" 
         
# Stock Price App

Below are the stock **closing price** and ***volume*** of the stock of your choice:""") 

#st.write(tickerSymbol)


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
#tickerSymbol = 'GOOGL'



tickerSymbol = st.text_input('', 'Input the Stock Symbol here to view price')


#get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start = '2010-5-31', end= '2020-5-31')
#Open High Low Close VOlume Dividends Stock Splits

st.write("""
## Closing Price
          """)
          
st.line_chart(tickerDf.Close)

st.write(""" 
## Volume Price
         """)
st.line_chart(tickerDf.Volume)


