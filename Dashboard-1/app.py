import streamlit as st

st.header("Button")

if st.button("ADD"):
    st.write("ADDITION")
else:
    st.write("SUBSTRACTION")