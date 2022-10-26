import streamlit as st

# import libraries

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from datetime import datetime


df= pd.read_csv("Aggregated_Metrics_By_Video.csv").iloc[1:, : ]

st.write(df)

# https://towardsdatascience.com/make-dataframes-interactive-in-streamlit-c3d0c4f84ccb


