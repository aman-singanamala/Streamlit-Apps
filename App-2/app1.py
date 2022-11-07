import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
import streamlit.components.v1 as components 



st.set_page_config(
    page_title= 'DiabetesPredictor' , 
    layout="wide", 
    initial_sidebar_state="expanded",
    page_icon="🧊"
    )


# Importing the dataset and splitting
df= pd.read_csv('https://raw.githubusercontent.com/aman-singanamala/Diabetes-Predictor/main/diabetes.csv')
X= df.iloc[:,[0,1,2,3,4,5,6,7]]
# Scaling the dataset
X= sc_X.fit_transform(X)

y= df.iloc[:, 8]





# containers

model_training = st.container()
dataset= st.container()


# sidebar


st.sidebar.header("Precautions")
estimators=st.sidebar.slider("n_estimators ( The number of trees in the forest.)",10,100, value=20)
max_depth=st.sidebar.selectbox("The maximum depth of the tree",options=[100,200,300,400,500,'No Limit'], index=2)# index = 0 means default value first element






st.title("Diabetes Prediction")
with st.expander("Expand Me 👈"):
    st.header("Know more about this feature")
    st.write("Inputs that need to be provides are:")
    st.markdown(
    '''
    - Number of Pregnancies
    '''
    )
    
    
    
# Inputs that need to be provides are:
col1 , col2 = st.columns(2)
with col1:
    st.subheader("Pregnancies")
    Pregnancies = st.slider("Input Your Number of Pregnancies", 0, 16, value= 2, step=1)
    st.subheader("Blood Pressure")
    BloodPressure = st.slider("Input your Blood Pressure",30,130, value=50, step=1)
    st.subheader("Insulin")
    Insulin = st.slider("Input your Insulin",0,200, value=50, step=1)
    st.subheader("DiabetesPedigreeFunction")
    DiabetesPedigreeFunction = st.slider("Input your Diabetes Pedigree Function",0.0,6.0)
with col2:
    st.subheader("Glucose Level")
    Glucose = st.slider("Input your Gluclose",74,200, value=90, step=1)
    st.subheader("Skin Thickness")
    SkinThickness = st.slider("Input your Skin thickness",0, 100, value= 50, step=1)
    st.subheader("Body Mass Index")
    BMI = st.slider("Input your BMI",14,60, value=25)
    st.subheader("Age")
    Age = st.slider("Input your Age",0, 100, value=26, step=1)
    
    

    

    
inputs=[[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]]

        
        
        
        
        
# Training The model with RandomForestClassifier
rfc= RandomForestClassifier(max_depth=max_depth, n_estimators=estimators)
rfc.fit(X,y)
prediction= rfc.predict(inputs)



st.markdown(
    "***"
)




if st.button("Predict"):
    result= rfc.predict(inputs)
    updated_res= result.flatten().astype(int)
    if updated_res ==0:
        with st.expander("Expand Me 👈"):
            st.write("Chances for getting Diabetes are less for you")
            st.header("Follow these habits for staying healthy")
            st.subheader("Eat healthy plant foods.")
            st.markdown("- Fruits, such as tomatoes, peppers and fruit from trees")
            st.markdown("- Nonstarchy vegetables, such as leafy greens, broccoli and cauliflower")
            st.markdown("Legumes, such as beans, chickpeas and lentils")
            st.markdown("Whole grains, such as whole-wheat pasta and bread, whole-grain rice, whole oats, and quinoa")
                        
            
            
    else:
        st.write("You are not safe, you might get Diabetes")
        with st.expander("Expand Me 👈"):
            st.header("")
            
            st.header("Follow these habits for staying healthy")
            st.subheader("Eat healthy plant foods.")
            st.markdown("- Fruits, such as tomatoes, peppers and fruit from trees")
            st.markdown("- Nonstarchy vegetables, such as leafy greens, broccoli and cauliflower")
            st.markdown("- Legumes, such as beans, chickpeas and lentils")
            st.markdown("- Whole grains, such as whole-wheat pasta and bread, whole-grain rice, whole oats, and quinoa")
            

            
        

    


