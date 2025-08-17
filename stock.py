import streamlit as st
import yfinance as yf

st.title("Stock price Analyzer")
ticker=st.text_input("Enter stock name to analyze","MSFT")
ticker_data=yf.Ticker(ticker)
sd=st.date_input("Enter start date")
ed=st.date_input("Enter end date")
ticker_df=ticker_data.history(start=sd,end=ed)
st.dataframe(ticker_df.head())

st.subheader("price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("volume movement over time")
st.bar_chart(ticker_df['Volume'])