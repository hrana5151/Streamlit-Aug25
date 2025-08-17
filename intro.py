import streamlit as st
st.title("Learning Streamlit")
st.header("amazing online web app creating tool")
st.write("takes simple codes to design beautiful front end app")
agree = st.checkbox ("tick if you like me")
if agree:
    st.write("you are amazing")
genre = st.radio("what is your fav genre", ["drama","Scifi","action"])
st.write(genre)