import streamlit as st
import plotly.express as px
import pandas as pd

# load your dataset
df = pd.read_csv("google-play-store-apps/googleplaystore.csv")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   
   # create the distplot using the column of values between 0 and 5
   fig = px.histogram(df, x='Rating', hover_data=df.columns, title="Distribution of Column Rating")
   fig.update_xaxes(range=[0, 5], tickformat=".1f")
   # display the plot
   st.plotly_chart(fig)



with col2:
   
   

   # create the kdeplot using the column of values between 0 and 5
   fig = px.density_heatmap(df, x='Rating',
                           title='KDE Plot of Values', hover_data=df.columns)

   # set x-axis range to only go up to 5
   fig.update_xaxes(range=[0, 5], tickformat=".1f")

   # display the plot
   st.plotly_chart(fig)