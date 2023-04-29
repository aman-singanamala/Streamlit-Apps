import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
from plotly.subplots import make_subplots
# Load data
data = pd.read_csv("./google-play-store-apps/googleplaystore.csv")

# Define function to preprocess data
def preprocess_data(df):
    # drop rows with missing values
    df.dropna(inplace=True)
    # convert "Last Updated" column to datetime
    df["Last Updated"] = pd.to_datetime(df["Last Updated"])
    # extract year and month from "Last Updated" column
    df['year_added'] = df['Last Updated'].dt.year
    df['month_added'] = df['Last Updated'].dt.month
    # convert "Reviews" column to integer format
    df['Reviews'] = df['Reviews'].apply(lambda x: int(x))
    return df

# Preprocess data
data = preprocess_data(data)

# Define sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Exploratory Data Analysis"])

# Define homepage
if page == "Homepage":
    st.title("Google Play Store Apps")
    st.write("This app analyzes data on Google Play Store apps.")
    st.write("Use the sidebar to navigate to different pages.")
    
# Define EDA page
elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")
    st.write("This page explores the Google Play Store apps dataset.")
    # display pie chart of app types
    col = "Type"
    grouped = data[col].value_counts().reset_index()
    grouped = grouped.rename(columns = {col : "count", "index" : col})
    trace = go.Pie(labels=grouped[col], values=grouped['count'], pull=[0.08, 0])
    layout = {'title': 'Target(0 = No, 1 = Yes)'}
    fig = go.Figure(data = [trace], layout = layout)
    st.plotly_chart(fig)

    st.write("#### Here we see that 92.6% apps are freee and 7.38% apps are paid on google playstore. so we say that Most of the people love free services")



    st.markdown("<hr>", unsafe_allow_html=True)



    d1 = data[data['Type'] == 'Free']
    d2 = data[data['Type'] == 'Paid']
    col = 'year_added'
    v1 = d1[col].value_counts().reset_index()
    v1 = v1.rename(columns={col: 'count', 'index': col})
    v1['percent'] = v1['count'].apply(lambda x: 100 * x / sum(v1['count']))
    v1 = v1.sort_values(col)
    v2 = d2[col].value_counts().reset_index()
    v2 = v2.rename(columns={col: 'count', 'index': col})
    v2['percent'] = v2['count'].apply(lambda x: 100 * x / sum(v2['count']))
    v2 = v2.sort_values(col)

    trace1 = go.Scatter(x=v1[col], y=v1['count'], name='Free', marker=dict(color='#a678de'))
    trace2 = go.Scatter(x=v2[col], y=v2['count'], name='Paid', marker=dict(color='#6ad49b'))
    y = [trace1, trace2]
    layout = {'title': 'App updated or added over the years', 'xaxis': {'title': 'Years'}}
    fig = go.Figure(data=y, layout=layout)

    st.plotly_chart(fig)

    st.write('''
    ## Analysis and Conclusion
    In the above plot, we compare the number of apps that have been updated or added over the course of the year (free vs paid).
    We can conclude from this plot that there were no paid apps prior to 2011 (after that, Google believes that people have a lot of money, 
    so why not charge for some apps >> just for fun). However, over the course of the year, a large number of free apps have been added 
    in comparison to paid apps - indicating that people dislike paid services.

    When comparing apps updated or added between 2011 and 2018, free apps increased from 80% to 96%, while paid apps decreased from 20% to 4%.
''')



    st.markdown("<hr>", unsafe_allow_html=True)


    import streamlit as st
    import plotly.graph_objs as go
    from plotly.offline import iplot

    col = 'month_added'
    d1 = data[data['Type'] == 'Free']
    v1 = d1[col].value_counts().reset_index()
    v1 = v1.rename(columns={col:'count','index':col})
    v1['percent'] = v1['count'].apply(lambda x : 100 * x / sum(v1['count']))
    v1 = v1.sort_values(col)
    trace1 = go.Bar(x = v1[col], y = v1['count'], name = 'Free', marker = dict())
    layout = {'title': 'Free App added over the month', 'xaxis': {'title': 'months'}}
    fig = go.Figure(data = [trace1], layout = layout)

    st.plotly_chart(fig)

    st.write('''
    This Google Playstore data Almost half of the apps available on the Play Store are added or updated in July, 25% in August, and the remaining 25% in the remaining months.
''')


    st.markdown("<hr>", unsafe_allow_html=True)    


    # plot bar chart for paid app added over the month
    col='month_added'
    v2=d2[col].value_counts().reset_index()
    v2=v2.rename(columns={col:'count','index':col})
    v2['percent']=v2['count'].apply(lambda x : 100*x/sum(v2['count']))
    v2=v2.sort_values(col)
    trace1 = go.Bar(x=v2[col], y=v2["count"], name="Paid", marker=dict())
    layout={'title':"Paid App added over the month",'xaxis':{'title':"months"}}
    fig = go.Figure(data=[trace1], layout=layout)

    # display plot in Streamlit
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)



    
    # Filter data by type
    d1 = data[data['Type']=='Free']

    # Count values by content rating
    col = 'Content Rating'
    v1 = d1[col].value_counts().reset_index()
    v1 = v1.rename(columns={col: 'count', 'index': col})
    v1['percent'] = v1['count'].apply(lambda x : 100*x/sum(v1['count']))
    v1 = v1.sort_values(col)

    # Create plot
    fig = make_subplots(rows=1, cols=1, subplot_titles=("Free App Content Rating"))

    # Add bar trace for free apps
    fig.add_trace(
        go.Bar(x=v1[col], y=v1["count"], name="Free", marker=dict()),
        row=1, col=1
    )

    # Set x-axis and y-axis titles
    fig.update_xaxes(title_text="Contents", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)

    # Set plot layout
    fig.update_layout(title="Free App Content Rating")

    # Display plot in Streamlit
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)



    col = 'Content Rating'
    d1 = data[data['Type'] == 'Free']
    d2 = data[data['Type'] == 'Paid']

    v1 = d1[col].value_counts().reset_index()
    v1 = v1.rename(columns={col:'count','index':col})
    v1['percent'] = v1['count'].apply(lambda x: 100 * x / sum(v1['count']))
    v1 = v1.sort_values(col)

    v2 = d2[col].value_counts().reset_index()
    v2 = v2.rename(columns={col:'count','index':col})
    v2['percent'] = v2['count'].apply(lambda x: 100 * x / sum(v2['count']))
    v2 = v2.sort_values(col)

    trace1 = go.Bar(x=v2[col], y=v2['count'], name='Paid', marker=dict(color='#6ad49b'))
    layout = go.Layout(title='Paid App Content Rating', xaxis=dict(title='Contents'))
    fig = go.Figure(data=[trace1], layout=layout)

    st.plotly_chart(fig)


    st.markdown("<hr>", unsafe_allow_html=True)


  

    # assume d1 contains the data for free apps

    col='Rating'
    v1=d1[col].value_counts().reset_index()
    v1=v1.rename(columns={col:'count','index':col})
    v1['percent']=v1['count'].apply(lambda x : 100*x/sum(v1['count']))
    trace1 = go.Bar(x=v1[col], y=v1["count"], name="Free", marker=dict())

    layout={'title':"Free App Rating",'xaxis':{'title':"Ratings"}}
    fig = go.Figure(data=[trace1], layout=layout)

    st.plotly_chart(fig)


    st.markdown("<hr>", unsafe_allow_html=True)


        
    # Filter the data to include only paid apps
    paid_data = data[data["Type"] == "Paid"]

    # Count the number of apps in each rating category
    col = "Rating"
    v2 = paid_data[col].value_counts().reset_index()
    v2 = v2.rename(columns={col:'count', 'index':col})
    v2['percent'] = v2['count'].apply(lambda x : 100*x/sum(v2['count']))
    v2 = v2.sort_values(col)

    # Create a plot using Plotly
    trace1 = go.Bar(x=v2[col], y=v2["count"], name="Paid", marker=dict(color="#6ad49b"))
    layout = {'title': "Paid App Rating", 'xaxis': {'title': "Ratings"}}
    fig = go.Figure(data=[trace1], layout=layout)

    # Display the plot in Streamlit
    st.plotly_chart(fig)



    st.markdown("<hr>", unsafe_allow_html=True)

    

    # Plot scatter plot
    col='Category'
    v1=d1[col].value_counts().reset_index()
    v1=v1.rename(columns={col:'count','index':col})
    v1['percent']=v1['count'].apply(lambda x : 100*x/sum(v1['count']))
    v1=v1.sort_values(col)
    v2=d2[col].value_counts().reset_index()
    v2=v2.rename(columns={col:'count','index':col})
    v2['percent']=v2['count'].apply(lambda x : 100*x/sum(v2['count']))
    v2=v2.sort_values(col)
    trace1 = go.Scatter(x=v1[col], y=v1["count"], name="Free", marker=dict(color="#a678de"))
    trace2 = go.Scatter(x=v2[col], y=v2["count"], name="Paid", marker=dict(color="#6ad49b"))
    y = [trace1, trace2]
    layout={'title':"App Category"}
    fig = go.Figure(data=y, layout=layout)

    st.plotly_chart(fig)


    st.markdown("<hr>", unsafe_allow_html=True)


    
    # Plot
    col='Android Ver'
    v1=d1[col].value_counts().reset_index()
    v1=v1.rename(columns={col:'count','index':col})
    v1['percent']=v1['count'].apply(lambda x : 100*x/sum(v1['count']))
    v1=v1.sort_values(col)
    v2=d2[col].value_counts().reset_index()
    v2=v2.rename(columns={col:'count','index':col})
    v2['percent']=v2['count'].apply(lambda x : 100*x/sum(v2['count']))
    v2=v2.sort_values(col)
    trace1 = go.Scatter(x=v1[col], y=v1["count"], name="Free", marker=dict(color="#a678de"))
    trace2 = go.Scatter(x=v2[col], y=v2["count"], name="Paid", marker=dict(color="#6ad49b"))
    y = [trace1, trace2]
    layout={'title':"Android Versions"}
    fig = go.Figure(data=y, layout=layout)

    # Display plot
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)
    


    # Plot installed app counts
    col='Installs'
    v1=d1[col].value_counts().reset_index()
    v1=v1.rename(columns={col:'count','index':col})
    v1['percent']=v1['count'].apply(lambda x : 100*x/sum(v1['count']))
    v1=v1.sort_values(col)
    v2=d2[col].value_counts().reset_index()
    v2=v2.rename(columns={col:'count','index':col})
    v2['percent']=v2['count'].apply(lambda x : 100*x/sum(v2['count']))
    v2=v2.sort_values(col)
    trace1 = go.Scatter(x=v1[col], y=v1["count"], name="Free", marker=dict(color="#a678de"))
    trace2 = go.Scatter(x=v2[col], y=v2["count"], name="Paid", marker=dict(color="#6ad49b"))
    y = [trace1, trace2]
    layout={'title':"Installed App ",'xaxis':{'title':"Installs"}}
    fig = go.Figure(data=y, layout=layout)

    # Render plot
    st.plotly_chart(fig)









