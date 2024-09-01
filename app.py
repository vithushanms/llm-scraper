import streamlit as st

st.title("Welcome to LLM-Scraper !")
st.text("An open-source web scraper powered by an LLM")

st.text_input("Enter the URL of the website you want to scrape")

if st.button("Scrape"):
    st.write("Scraping the website...")
