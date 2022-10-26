import streamlit as st
import pyshorteners as ps



st.header("URL Shortener")

st.image("i1.png")
url= st.text_input("Enter your URL : (Example: http://example.com)", value="amansinganamala.medium.com/statistics-concepts-in-data-science-bffe06d56de6")

ans= ps.Shortener().tinyurl.short(url)

if ans != '':
    st.write(f"Your shortened URL:{ans}")
else:
    st.write("Enter your url")
    
    
    
    

st.write("Note: Remove the link in input field and paste your URL into the Input Field")