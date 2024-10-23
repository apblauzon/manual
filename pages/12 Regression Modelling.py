import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import statsmodels.api as sm
from scipy.stats import chi2_contingency

st.set_page_config(page_title="DatViz Ai | Regression Modelling", page_icon="logo.svg")
df = pd.read_csv('new_data.csv')
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%d/%m/%Y')
df['MonthYear'] = df['TransactionDate'].dt.to_period('M')
monthly_data = df.groupby('MonthYear').agg({'Quantity': 'sum', 'TotalAmount': 'sum','Price': 'mean'}).reset_index()


diabetes = pd.read_csv("diabetes.csv")


# Streamlit app
def show_hypothesis_testing():
    st.header("Regression Modelling")
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
    st.write("**PROMPT: Generate a linear regression with the monthly total amount as the dependent variable, and the monthly quantity and average monthly price as independent variables. Display the regression equation and two dimensional graph.**")
    st.write("")
    st.write(f"**Regression Equation:** {regression_equation}")
    st.write("")
    st.plotly_chart(fig, use_container_width=True)
    st.write("")
    
    X = diabetes[['Glucose']]
    y = diabetes['Outcome']

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Prediction probabilities
    diabetes['Probability'] = model.predict_proba(scaler.transform(diabetes[['Glucose']]))[:, 1]
    st.write("**PROMPT: Generate logistic regression with outcome as dependent variable and glucose as independent variable.**")
    # Ensure the 'Probability' column is in the DataFrame
    if 'Probability' in diabetes.columns:
        # Plot
        fig = px.scatter(diabetes, x='Glucose', y='Probability', color='Outcome',
                        labels={'Probability': 'Predicted Probability of Diabetes'},
                        title='Logistic Regression Prediction on Glucose Levels')
        fig.update_traces(marker=dict(size=10))
        fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Probability column not found in the DataFrame.")
    st.text("Note: Using diabetes.csv (from Kaggle)")
    st.write("")
# Display the hypothesis testing results
show_hypothesis_testing()

