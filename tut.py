from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import altair as alt
from turtle import color
import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np

st.code(
    """
    [theme]
    primaryColor = "#03d3fc"
    backgroundColor="#2E86C1"
    secondaryBackgroundColor="#AED6F1"
    textColor="#FFFFFF"
    font="monospace"
    """
)

st.header("slider")

# Example 1

st.subheader("slider")

age = st.slider("How old are you?", 0, 100, 25)

st.write("I am ", age, "Years old")

# Example 2

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)

)
st.write("Selected range :  ", values)


# Example 3

st.subheader("Range time slider")

appointment = st.slider(
    "Sechedule your appointment",
    value=(time(11, 30), time(12, 45))
)


# Example 4

st.header("Line Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)


# Example 5

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']

)

c = alt.Chart(df).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


# Day 10
# selectbox
st.header("st.selectbox")

option = st.selectbox(
    'What is your name?',
    ('Blue', 'Red', 'Green')
)
st.write('Your favourite color is ', option)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# EXample 6
# Columns

col1, cols2 = st.columns(2)
col1.write('This is column 1')
cols2.write('This is column 2')

# THREE SIFFERENT COLUMNS
col1, col2, col3 = st.columns([3, 1, 1])  # column1 is larger
# Use 'with' notation
with col1:
    ans = st.radio('Select one:', [1, 2])
    st.write("You selected:", ans)

# EXample 7
# Tabs

tab1, tab2 = st.tabs(['Tab1', 'Tab2'])

with tab1:
    st.write("The informations that is present in the tab1 is here")
    st.radio('Select one:', ['Aman', 'Singanamala'])
with tab2:
    st.write("The informations that is present in the tab2 is here")


# Day 11

st.header('st.multiselect')

options = st.multiselect(
    'Programming languages you like to learn',
    ['Python', 'Java', 'C', 'C++'],
    ['C++', 'Java']
)
st.write("You like to learn: ", options)


# Day 12
# Check box
st.header("st.checkbox")
st.write("What would you like to order?")

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write(" Ice cream is available")
if coffee:
    st.write(" coffee is available")
if cola:
    st.write(" cola is available")

# Day 14


# st.header("streamlit_pandas_profiling")

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/aman-singanamala/Predictors/main/Diabetes/file.csv")

# pr = df.profile_report()

# st_profile_report(pr)



# Layout
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
  
  
st.sidebar.header("GIve inputs here:")

username= st.sidebar.text_input("Name:")


userheight= st.sidebar.number_input("Your height: (in feet):")

col1 , col2 = st.columns(2)

with col1:
    if username!="":
        st.write(f"Hello {username}!")
    else:
        st.write("Please enter your username")
with col2:
    if userheight!="":
        st.write(f"Height is {userheight}")
    else:
        st.write("Please enter yout height")
    
    
    
    
# st.progress

import streamlit as st
import time

st.title("st.progress")


# with st.expander("ABout this page"):
#     st.write("Progress informations is shown here ")
    
# my_bar= st.progress(0)

# for i in range(100):
#     time.sleep(0.10)
#     my_bar.progress(i+1)
    
    
    
# st.balloons()

# st.form

st.write("forms")

with st.form("form"):
    st.write("**Order yout coffee**")
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    submitted = st.form_submit_button('Submit')
    


if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
    
    
    
    
