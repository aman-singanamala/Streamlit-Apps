
## About Me 👩‍💻

<p><img src="Images\aman.png" width=100/></p>

Hello 👋 

I am Aman Singanamala, Computer Science Student pursuing my Bachelors degree at Vellore Institute of Technology 🖥️

#### ***Socials*** 

[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/amansinganamala)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amansinganamala)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aman-singanamala)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](amansinganamala@gmail.com)
[![Medium](https://img.shields.io/badge/-Medium-black?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@amansinganamala)



### This is my Portfolio of collection of all Streamlit application I made. 🙂






<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100">

***The Streamlit application that are included are:***

1. URL Shortener
2. Weather Dashboard
3. Diabeted Predictor
4. Analysis of Google Play Store Application

... more (Updating soon)


**About the Streamlit apps**


<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" width="100" height="100">


---
---


## [1. URL Shortener](./URL_SHORTENER/README.md) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tinyurl.com/28qq4x24)  

   - This used the streamlit framework anf PyShortners library to create a URL shortener web application.
   - Overall, this program provides a simple and user-friendly interface for generating shortened URLs using PyShorteners and Streamlit.

<p align="center"><img src="URL_SHORTENER\i1.png" width=500/></p>





---
---


## [2. Weather Dashboard](./Weather-Dashboard/README.md) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-streamlit-apps-app-1app-lrxr52.streamlitapp.com/) 


   - This Streamlit application provides the user with several functionalities for exploring and visualizing datasets.
   - The program creates a sidebar that allows the user to customize the parameters for the heatmap, donut chart, and line chart. The user can select which columns to use for coloring the heatmap, selecting data for the donut chart, and choosing which columns to display in the line chart. The user can also customize the height of the line chart.
   - The heatmap displays the median temperature in Seattle for each day of the week over time, while the donut chart shows stock values for various companies. The line chart displays the trend of temperature in Seattle over time.
   - Provides an interactive web interface for visualizing the datasets with various customizable options, making it easy for the user to gain insights and explore data trends in a user-friendly manner.

<p align="center"><img src="Images\dashboard.png" width=500/></p>




---
---

## [3. Diabeted Predictor](./Diabetes-Predictor/README.md) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-streamlit-apps-diabetes-predictorapp1-dltfg9.streamlit.app/) 


   - Web application that predicts the chances of a person getting diabetes using the Random Forest Classifier algorithm.
   - The application takes in eight inputs: Number of Pregnancies, Glucose Level, Blood Pressure, Skin Thickness, Insulin, Body Mass Index (BMI), Diabetes Pedigree Function, and Age. The user can adjust these inputs using sliders provided in the web interface.
   - Once the user inputs are provided, the model predicts the chances of the person getting diabetes. The predicted result is displayed on the web interface as well as advice on how to stay healthy based on the predicted result.
   - The web application is built using the Streamlit library, which provides a simple way to build web applications in Python. It also makes use of the Pandas library for data manipulation, the Scikit-learn library for the Random Forest Classifier algorithm, and the StandardScaler function for data scaling.
   - The web application is designed to be user-friendly and interactive, with expandable sections and slider inputs. It provides valuable insights to users on how to stay healthy based on their predicted chances of getting diabetes.


<p align="center"><img src="Diabetes-Predictor\i1.png" width=500/></p>

---





---

## [4. Analysis of Google Play Store Applications](./Google_Play_Store_Apps/README.md)

<p align="center"><img src="./Google_Play_Store_Apps/PLOTS/dataset-cover.jpg" width=500/></p>



- ## Visualization Website 1: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-sin-jcomp-vis-ni485h.streamlit.app)  

- ## Visualization Website 2: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-sin-jcomp-app-lih7o2.streamlit.app)  
- ## Dataset: https://www.kaggle.com/datasets/lava18/google-play-store-apps
- ## Modeling Notebook : 




## Data Cleaning

The dataset contained missing values and duplicates, which were handled using pandas methods. 

## Exploratory Data Analysis

The analysis includes the following findings:

- Most users gave a rating between 4 and 5 with a count of 7049.
- The average rating of applications in the store is around 4 which is very high.
- Game and Family category are the most appearances for applications in the store.
- Beauty and Events are the least most appearances for applications in the store.
- The ratings of applications in each category are relatively similar, with an average rating above 4.
- Most applications in this store have less than 1 million reviews. Well-known applications have a lot of reviews.

## Visualization

The analysis is presented in two Streamlit apps, which can be accessed using the links provided above.

## Modeling 
<iframe src="./Google_Play_Store_Apps/modeling.html" width="100%" height="500"></iframe>


Model Selection and Hyperparameter Tuning

## Description

We utilized the Support Vector Machine (SVM) algorithm as our model of choice due to its ability to handle high dimensional data and its effectiveness in classification tasks. We implemented the SVM model using scikit-learn's SVC class, which allows us to specify the kernel function and hyperparameters.

To optimize the performance of our SVM model, we employed a pipeline that consists of several steps:

<b> 1. Custom Transformer:</b> This is a custom transformation step that applies a transformation to the data. We passed a parameter "5" to the Custom Transformer class to customize the transformation.

<b> 2. StandardScaler: </b> This step scales the data to have zero mean and unit variance, which is an important step for many machine learning algorithms to work effectively.

<b>3. GridSearchCV: </b> This step performs grid search cross-validation to find the best hyperparameters for the SVM model. We optimized the hyperparameters 'C', 'kernel', and 'gamma' with a range of values specified in the 'param_grid' dictionary. The model was trained using 5-fold cross-validation, and the best hyperparameters were selected based on the average test score.

- After defining the pipeline, we fit the pipeline on the training data using the fit method. We then printed the results for each permutation of hyperparameters tested in the grid search using a for loop. The loop iterated over the mean_train_score, mean_test_score, and params values from the GridSearchCV results.

- Finally, we printed the best score and best hyperparameters for the SVM model found during the grid search. This allowed us to select the optimal hyperparameters for our SVM model, which helped to improve its performance on the test data.

- Overall, this approach for tuning hyperparameters for a machine learning model using cross-validation is a common and effective way to optimize model performance.


## Conclusion

This analysis provides insights into the Google Play Store apps dataset and can be used by developers and businesses to make data-driven decisions.










---
---
