import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
st.set_page_config(layout="wide")


# load your dataset
df = pd.read_csv("google-play-store-apps/googleplaystore.csv")
df.dropna(how='any', inplace=True)



col1, col2 = st.columns(2)



# -----------------------------------------------------------------------------------
# rating
# create the distplot using the column of values between 0 and 5
fig1 = px.histogram(
   df, 
   x='Rating', hover_data=df.columns,
   title="Distribution of Column Rating",
   opacity=0.8
   
   )
fig1.update_xaxes(range=[0, 5], tickformat=".1f")
fig1.update_xaxes(gridcolor='lightgray', gridwidth=1)
fig1.update_yaxes(gridcolor='lightgray', gridwidth=1)
# display the plot
st.plotly_chart(fig1)

st.write("### Finding-1")
st.write("- Most users gave a rating between 4 and 5 with a count of 7049")
st.write("- Average rating of the application in the store is around 4, which is very high")


# -----------------------------------------------------------------------------------

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)





# -----------------------------------------------------------------------------------
# catregory
x = ['FAMILY', 'GAME', 'TOOLS', 'PRODUCTIVITY', 'MEDICAL', 'COMMUNICATION',
     'FINANCE', 'SPORTS', 'PHOTOGRAPHY', 'LIFESTYLE', 'PERSONALIZATION',
     'BUSINESS', 'HEALTH_AND_FITNESS', 'SOCIAL', 'SHOPPING',
     'NEWS_AND_MAGAZINES', 'TRAVEL_AND_LOCAL', 'DATING',
     'BOOKS_AND_REFERENCE', 'VIDEO_PLAYERS', 'EDUCATION', 'ENTERTAINMENT',
     'MAPS_AND_NAVIGATION', 'FOOD_AND_DRINK', 'HOUSE_AND_HOME', 'WEATHER',
     'AUTO_AND_VEHICLES', 'LIBRARIES_AND_DEMO', 'ART_AND_DESIGN', 'COMICS',
     'PARENTING', 'EVENTS', 'BEAUTY']
y = [1746, 1097, 733, 351, 350, 328, 323, 319, 317, 314, 312, 303, 297, 259, 238,
     233, 226, 195, 178, 160, 155, 149, 124, 109, 76, 75, 73, 64, 61, 58, 50, 45, 42]

# Create the figure
fig2 = go.Figure(data=[go.Bar(x=y, y=x, orientation='h')])
# Update the layout
fig2.update_layout(
    title='Category vs Rating',
    xaxis_title='Rating',
    yaxis_title='Category',
    width=1000,
    height=1000,
    margin=dict(l=200, r=50, t=100, b=100),
)
st.write(fig2, use_container_width=True)

# -----------------------------------------------------------------------------------



st.write("### Finding-2")
st.write("- Game and Family category are the most appearances for applications in the store.")
st.write("- Beauty and Events are the least most appearances for applications in the store.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Display the code to get unique values in the Category column
st.write("### Column ['Category']")
st.write("#### Get the unique values in the column with its frequency using the below code:")
st.code("""categories=(df['Category'].value_counts())
type(categories) ## to know its structure == Series type
# convert the categories into a dataframe
categories.to_frame()
""", language='python')

# Display the table with unique values and their frequencies
st.write("### Output")
categories = pd.DataFrame({
    "Category": ["FAMILY", "GAME", "TOOLS", "PRODUCTIVITY", "MEDICAL", "COMMUNICATION", "FINANCE", "SPORTS", 
                 "PHOTOGRAPHY", "LIFESTYLE", "PERSONALIZATION", "BUSINESS", "HEALTH_AND_FITNESS", "SOCIAL", "SHOPPING", 
                 "NEWS_AND_MAGAZINES", "TRAVEL_AND_LOCAL", "DATING", "BOOKS_AND_REFERENCE", "VIDEO_PLAYERS", 
                 "EDUCATION", "ENTERTAINMENT", "MAPS_AND_NAVIGATION", "FOOD_AND_DRINK", "HOUSE_AND_HOME", "WEATHER", 
                 "AUTO_AND_VEHICLES", "LIBRARIES_AND_DEMO", "ART_AND_DESIGN", "COMICS", "PARENTING", "EVENTS", "BEAUTY"],
    "Count": [1746, 1097, 733, 351, 350, 328, 323, 319, 317, 314, 312, 303, 297, 259, 238, 233, 226, 195, 178, 
              160, 155, 149, 124, 109, 76, 75, 73, 64, 61, 58, 50, 45, 42]
})
st.write(categories)



st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------------
# category vs rating
fig = px.box(
   df, 
   x=df['Category'], 
   y=df['Rating'], 
   width=1000, 
   height=500,
   range_y=[0,5]
   )
fig.update_xaxes(gridcolor='lightgray', gridwidth=1)
fig.update_yaxes(gridcolor='lightgray', gridwidth=1)
st.plotly_chart(fig)
# -----------------------------------------------------------------------------------





st.write("### Finding-3")
st.write("- The ratings of applications in each category are relatively similar, with an average rating above 4.")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)




# --------------------------------------------------------------
import streamlit as st
import plotly.express as px

labels= ['Instagram', 'WhatsApp Messenger',
       'Messenger – Text and Video Chat for Free', 'Facebook']
values=[4,3,3,2]



fig= px.pie(labels, values=values, names= labels, hole=0.5)
st.plotly_chart(fig)
# --------------------------------------------------------------



st.write("### Finding-4")
st.write("- Most applications in this store have less than 1 million reviews.")
st.write("- Well-known applications have a lot of reviews.")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)