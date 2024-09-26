import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import scipy.stats as stats


df = pd.read_csv('new_data.csv')
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%d/%m/%Y')
df['MonthYear'] = df['TransactionDate'].dt.to_period('M')
monthly_data = df.groupby('MonthYear').agg({'Quantity': 'sum', 'TotalAmount': 'sum','Price': 'mean'}).reset_index()


# Streamlit app
def show_hypothesis_testing():
    st.title("Statistics Test")
    st.header("Linear Regression")
    st.markdown("""
    Regression analysis is a statistical technique used to understand the relationship between a dependent variable and one or more independent variables. It helps in predicting outcomes and identifying significant predictors. Common types of regression include linear regression, multiple regression, and logistic regression.
    """)

    X = monthly_data[['Quantity', 'Price']]
    y = monthly_data['TotalAmount']
    reg = LinearRegression().fit(X, y)
    monthly_data['Predicted_TotalAmount'] = reg.predict(X)
    intercept = reg.intercept_
    coef_quantity, coef_price = reg.coef_
    regression_equation = f'Total Amount = {intercept:.2f} + {coef_quantity:.2f} * Quantity + {coef_price:.2f} * Price'

    fig = px.scatter(monthly_data, x='Quantity', y='TotalAmount', title='Monthly Total Amount vs. Quantity', labels={'Quantity': 'Total Quantity', 'TotalAmount': 'Total Amount'}, trendline='ols', trendline_color_override='darkblue')
    fig.update_layout(
    template='simple_white',
    title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis=dict(
        title='Total Quantity',
        titlefont_size=14),
    yaxis=dict(
        title='Total Amount',
        titlefont_size=14)
)
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.write("")
    st.write(f"**Regression Equation:** {regression_equation}")
    st.write("")
    st.plotly_chart(fig, use_container_width=True)
    
# Display the hypothesis testing results
show_hypothesis_testing()

