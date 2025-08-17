import streamlit as st
import yfinance as yf

st.title("Stock price Analyzer")
col1,col2,col3 = st.columns(3)
with col1:
    ticker=st.text_input("Enter stock name to analyze","MSFT")
    ticker_data=yf.Ticker(ticker)
with col2:
    sd=st.date_input("Enter start date")
with col3:
    ed=st.date_input("Enter end date")
ticker_df=ticker_data.history(start=sd,end=ed)
st.dataframe(ticker_df.head())

st.subheader("price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("volume movement over time")
st.bar_chart(ticker_df['Volume'])