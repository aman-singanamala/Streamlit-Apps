from turtle import color
import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np

st.header("slider")

# Example 1

st.subheader("slider")

age= st.slider("How old are you?",0,100,25)

st.write("I am ", age,"Years old")

# Example 2

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0,75.0)
    
)
st.write("Selected range :  ", values)


# Example 3

st.subheader("Range time slider")

appointment = st.slider(
    "Sechedule your appointment",
    value=(time(11,30), time(12,45))
)


# Example 4

st.header("Line Chart")

chart_data= pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)


# Example 5

import altair as alt
df= pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
             
)

c=alt.Chart(df).mark_circle().encode(
    x='a', 
    y='b',
    size='c',
    color='c',
    tooltip=['a','b','c'])

st.altair_chart(c, use_container_width=True)


# Day 10
# selectbox
import streamlit as st
st.header("st.selectbox")

option= st.selectbox(
    'What is your name?',
    ('Blue','Red','Green')
)
st.write('Your favourite color is ', option)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# EXample 6 
## Columns

import streamlit as st
col1, cols2 = st.columns(2)
col1.write('This is column 1')
cols2.write('This is column 2')

# THREE SIFFERENT COLUMNS
col1, col2, col3= st.columns([3,1,1]) # column1 is larger
# Use 'with' notation
with col1:
    ans=st.radio('Select one:', [1,2])
    st.write("You selected:", ans)
    
# EXample 7
# Tabs

tab1, tab2= st.tabs(['Tab1', 'Tab2'])

with tab1:
    st.write("The informations that is present in the tab1 is here")
    st.radio('Select one:', ['Aman', 'Singanamala'])
with tab2:
    st.write("The informations that is present in the tab2 is here")


# Day 11

import streamlit as st
st.header('st.multiselect')

options= st.multiselect(
    'Programming languages you like to learn',
    ['Python', 'Java', 'C','C++'],
    ['C++', 'Java']
)
st.write("You like to learn: ", options)


# Day 12
# Check box
st.header("st.checkbox")
import streamlit as st
st.write("What would you like to order?")

icecream= st.checkbox('Ice cream')
coffee= st.checkbox('Coffee')
cola= st.checkbox('Cola')

if icecream:
    st.write(" Ice cream is available")
if coffee:
    st.write(" coffee is available")
if cola: 
    st.write(" cola is available")
    
# Day 14

import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header("streamlit_pandas_profiling")

df= pd.read_csv("https://raw.githubusercontent.com/aman-singanamala/Predictors/main/Diabetes/file.csv")

pr= df.profile_report()

st_profile_report(pr)