# 🚗 Car Dataset - Exploratory Data Analysis (EDA)

This project provides a complete exploratory data analysis (EDA) on a car dataset using Python. The analysis covers various numerical and categorical features to understand the structure and insights hidden within the data.

## 📊 Dataset Overview
The dataset includes information about cars with features such as:

- Price
- Manufacturer and model
- Production year
- Fuel type
- Gearbox type
- Drive wheels
- Engine volume
- Mileage
- Number of doors, airbags, and cylinders
- Interior material and car color

## 🎯 Project Objectives

- Explore and visualize the distribution of each feature
- Identify trends and correlations
- Detect and interpret outliers
- Prepare insights for future modeling or decision-making

## 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📈 Key Analysis Tasks

- Statistical summaries of the dataset
- Univariate and multivariate analysis
- Boxplots, histograms, and scatterplots
- Correlation heatmap
- Category vs. Price visualizations

## 👤 Target Audience

This notebook is ideal for:

- Data science students
- Analysts interested in the automotive market
- Developers building price prediction or car classification models
- # 🚘 Car Dataset - Exploratory Data Analysis (EDA)

This notebook provides an in-depth exploratory data analysis of a car dataset, including both **numerical** and **categorical** features.

### Goals:
- Understand the distribution of car attributes
- Visualize patterns and relationships between variables
- Detect and handle outliers
- Gain insights useful for future machine learning models

### Main Columns:
- **Numerical:** Price, Levy, Production Year, Engine Volume, Mileage, Cylinders, Doors, Airbags
- **Categorical:** Manufacturer, Model, Category, Fuel Type, Gearbox Type, Drive Wheels, Interior, Wheel position, Color

## 🤖 Machine Learning Models & Results

After completing the exploratory data analysis (EDA), we trained several machine learning models to predict car prices based on both numerical and categorical features.

### 🔍 Models Applied

- **Linear Regression**
- **Polynomial Regression**
- **Lasso Regression**
- **Ridge Regression**
- **SVR**
- **Random Forest Regressor**
- **KNN Regression**
- **Decision Tree Regressor**
- **MLP Regression**

### 🧪 Evaluation Metrics

We used the following metrics to evaluate model performance:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

### 🏆 Best Model

- **Model:** Random Forest Regressor  
- **R² Score:** `0.7816`  
- **RMSE:** `28563870.108`  
- **MAE:** `3664.1695`  

This model outperformed others due to its ability to handle non-linear relationships and categorical variables effectively without requiring heavy preprocessing.

### 📌 Notes

- Features were encoded and scaled appropriately before modeling.
- Hyperparameter tuning was done using `GridSearchCV`, `RandomizedSearchCV` for optimized performance.
- Data was split into 80% training and 20% testing sets.

> The modeling phase added predictive power to the analysis and helped validate the importance of key features such as mileage, production year, engine volume, and car brand.
> Use Streamlit for Evaluation 
