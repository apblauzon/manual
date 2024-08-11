import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px

# Generate or load the dataset
np.random.seed(42)

# Generate synthetic data
n_rows = 1000
regions = ['North', 'South', 'East', 'West']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = [2022, 2023]
advertising_expenditure = np.random.uniform(1000, 10000, n_rows)
data_regression = {
    'Region': np.random.choice(regions, n_rows),
    'Sales': np.random.randint(500, 2000, n_rows),
    'Revenue': np.random.randint(1000, 5000, n_rows),
    'Month': np.random.choice(months, n_rows),
    'Year': np.random.choice(years, n_rows),
    'Advertising_Expenditure': advertising_expenditure
}

df_regression = pd.DataFrame(data_regression)

# Save the dataset to CSV
df_regression.to_csv('regression_data.csv', index=False)

# Streamlit app
def show_regression():
    st.header("Regression Analysis")
    st.markdown("""
    Regression analysis is a statistical technique used to understand the relationship between a dependent variable and one or more independent variables. It helps in predicting outcomes and identifying significant predictors. Common types of regression include linear regression, multiple regression, and logistic regression.
    """)

    # Load the dataset
    df = pd.read_csv('regression_data.csv')

    # Linear Regression: Predict Sales based on Advertising Expenditure
    st.subheader("Linear Regression: Predict Sales Based on Advertising Expenditure")
    st.write("Output:")
    
    X = df[['Advertising_Expenditure']]
    y = df['Sales']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and fit the model
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    
    # Predict and evaluate the model
    y_pred = linear_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    st.write("Mean Squared Error:", mse)
    st.write("Coefficients:", linear_model.coef_)
    st.write("Intercept:", linear_model.intercept_)
    
    # Plotting the regression line
    fig_linear = px.scatter(df, x='Advertising_Expenditure', y='Sales', trendline='ols',
                            title='Linear Regression of Sales vs. Advertising Expenditure')
    st.plotly_chart(fig_linear)

    # Multiple Regression: Understand the impact of various factors on Revenue
    st.subheader("Multiple Regression: Impact of Various Factors on Revenue")
    st.write("Output:")
    
    # Prepare data for multiple regression
    X_multi = df[['Advertising_Expenditure']]  # Add more features if needed
    y_multi = df['Revenue']
    
    # Split the data into training and testing sets
    X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)
    
    # Create and fit the model
    multi_model = Ridge(alpha=1.0)  # Ridge regression to avoid overfitting
    multi_model.fit(X_train_multi, y_train_multi)
    
    # Predict and evaluate the model
    y_pred_multi = multi_model.predict(X_test_multi)
    mse_multi = mean_squared_error(y_test_multi, y_pred_multi)
    
    st.write("Mean Squared Error (Multiple Regression):", mse_multi)
    st.write("Coefficients (Multiple Regression):", multi_model.coef_)
    st.write("Intercept (Multiple Regression):", multi_model.intercept_)
    
    # Plotting the regression results
    fig_multi = px.scatter(df, x='Advertising_Expenditure', y='Revenue', trendline='ols',
                          title='Multiple Regression of Revenue vs. Advertising Expenditure')
    st.plotly_chart(fig_multi)

# Display the regression results
show_regression()
