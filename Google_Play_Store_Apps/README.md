# Google Play Store App Analysis
<p><img src="./PLOTS/dataset-cover.jpg" width=1000/></p>

This project analyzes the Google Play Store apps dataset, which can be found on Kaggle [here](https://www.kaggle.com/lava18/google-play-store-apps). The analysis includes data cleaning, exploratory data analysis, and visualizations.

## Project Links

- ## GitHub Repository: https://github.com/aman-singanamala/SIN-JCOMP
- ## Visualization Website 1: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-sin-jcomp-vis-ni485h.streamlit.app)  

- ## Visualization Website 2: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aman-singanamala-sin-jcomp-app-lih7o2.streamlit.app)  
- ## Dataset: https://www.kaggle.com/datasets/lava18/google-play-store-apps




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
