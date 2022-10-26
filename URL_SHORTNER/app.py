import streamlit as st
import pyshorteners as ps

st.header("URL Shortener")


url= st.text_input("Enter your URL")

ans= ps.Shortener().tinyurl.short(url)

if ans != '':
    st.write(f"Your shortened URL:{ans}")
else:
    st.write("Enter your url")