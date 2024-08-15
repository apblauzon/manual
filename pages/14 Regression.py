import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import statsmodels.api as sm

# Load and update the dataset
df = pd.read_csv('aggregation_data.csv')
np.random.seed(42)
df['Discount Percentage'] = np.random.uniform(5, 50, len(df))
df['Profit'] = df['Discount Percentage'] * 1000
df['Quantity Sold'] = np.random.randint(1, 100, len(df))
df['Customer Lifetime Value'] = 10000 / df['Quantity Sold']
df.to_csv('updated_aggregation_data.csv', index=False)

# Streamlit app
def show_regression():
    st.header("Regression Analysis")
    st.markdown("""
    Regression analysis is a statistical technique used to understand the relationship between a dependent variable and one or more independent variables. It helps in predicting outcomes and identifying significant predictors. Common types of regression include linear regression, multiple regression, and logistic regression.
    """)

    # Polynomial Regression: Predict Profit based on Discount Percentage
    st.subheader("Polynomial Regression: Predict Profit Based on Discount Percentage")
    monthly_data = df.groupby(['Year', 'Month'])[['Sales', 'Orders']].sum().reset_index()
    monthly_data['Month'] = pd.Categorical(monthly_data['Month'], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], ordered=True)
    monthly_data = monthly_data.sort_values(['Year', 'Month'])

    X = monthly_data['Orders']
    y = monthly_data['Sales']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    p_values = model.pvalues
    equation = f"y = {model.params[0]:.2f} + {model.params[1]:.2f}x"
    is_significant = p_values[1] < 0.05

    fig = px.scatter(monthly_data, x='Orders', y='Sales', trendline="ols", title="Monthly Sales vs. Monthly Orders")
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8')),
                                    dict(x=0.7, y=0.1, xref='paper', yref='paper', xanchor='left', yanchor='bottom', text=equation, showarrow=False, font=dict(color='black'))])

    st.write(f"The regression equation is: {equation}")
    st.write(f"Is the relationship statistically significant? {'Yes' if is_significant else 'No'}")
    st.plotly_chart(fig, use_container_width=True)


    st.write("")
    st.write("")
    
    # Polynomial Regression: Predict Customer Lifetime Value based on Quantity Sold
    st.subheader("Polynomial Regression: Predict Customer Lifetime Value Based on Quantity Sold")
    
    X_clv = df[['Quantity Sold']]
    y_clv = df['Customer Lifetime Value']
    
    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_poly_clv = poly.fit_transform(X_clv)
    
    # Split the data into training and testing sets
    X_train_clv, X_test_clv, y_train_clv, y_test_clv = train_test_split(X_poly_clv, y_clv, test_size=0.2, random_state=42)
    
    # Create and fit the model
    poly_model_clv = LinearRegression()
    poly_model_clv.fit(X_train_clv, y_train_clv)
    
    # Predict and evaluate the model
    y_pred_clv = poly_model_clv.predict(X_test_clv)
    mse_clv = mean_squared_error(y_test_clv, y_pred_clv)
    
    st.write(f"Mean Squared Error: {mse_clv:.2f}")
    st.write(f"Coefficients: {poly_model_clv.coef_}")
    st.write(f"Intercept: {poly_model_clv.intercept_:.2f}")
    
    # Plotting the polynomial regression line
    df_sorted_clv = df.sort_values('Quantity Sold')
    X_sorted_clv = df_sorted_clv[['Quantity Sold']]
    X_poly_sorted_clv = poly.transform(X_sorted_clv)
    y_pred_sorted_clv = poly_model_clv.predict(X_poly_sorted_clv)
    
    fig_clv = px.scatter(df, x='Quantity Sold', y='Customer Lifetime Value', trendline='ols',
                        title='Polynomial Regression of Customer Lifetime Value vs. Quantity Sold')
    fig_clv.add_scatter(x=df_sorted_clv['Quantity Sold'], y=y_pred_sorted_clv, mode='lines', name='Polynomial fit')
    st.plotly_chart(fig_clv)

# Display the regression results
show_regression()
