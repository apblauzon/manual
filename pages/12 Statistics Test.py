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


# Seed for reproducibility
np.random.seed(42)

# Generate or load the dataset
n_rows = 1000
regions = ['North', 'South', 'East', 'West']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = [2022, 2023]
customer_names = [f'Customer_{i}' for i in range(n_rows)]
product_categories = ['Category_1', 'Category_2', 'Category_3']

# Generating random data
data_aggregation = {
    'Region': np.random.choice(regions, n_rows),
    'Sales': np.random.randint(500, 2000, n_rows),
    'Orders': np.random.randint(5, 25, n_rows),
    'Revenue': np.random.randint(1000, 5000, n_rows),
    'Month': np.random.choice(months, n_rows),
    'Year': np.random.choice(years, n_rows),
    'Latitude': np.random.uniform(-90, 90, n_rows),
    'Longitude': np.random.uniform(-180, 180, n_rows),
    'Customer_Name': np.random.choice(customer_names, n_rows),
    'Product_Category': np.random.choice(product_categories, n_rows),
    'Marketing_Campaign': np.random.choice(['Before', 'After'], n_rows)  # Added column for Marketing Campaign
}

df_aggregation = pd.DataFrame(data_aggregation)

# Save the dataset to CSV
df_aggregation.to_csv('aggregation_data.csv', index=False)

# Streamlit app
def show_hypothesis_testing():
    st.title("Statistics Test")
    st.header("Hypothesis Testing")
    st.markdown("""
    Hypothesis testing is a statistical method used to make inferences or draw conclusions about a population based on sample data. It involves formulating a null hypothesis and an alternative hypothesis, then using statistical tests to determine if there is enough evidence to reject the null hypothesis. Common tests include t-tests and chi-squared tests.
    """)

    # Load the dataset
    df = pd.read_csv('aggregation_data.csv')

    # Example 1: Compare average Sales before and after a marketing campaign
    st.subheader("Compare Average Sales Before and After a Marketing Campaign")
    st.write("Output:")
    before_campaign = df[df['Marketing_Campaign'] == 'Before']['Sales']
    after_campaign = df[df['Marketing_Campaign'] == 'After']['Sales']
    
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(before_campaign, after_campaign)
    
    st.write(f"T-Statistic: {t_stat:.4f}")
    st.write(f"P-Value: {p_value:.4f}")
    
    if p_value < 0.05:
        st.write("There is a significant difference in average sales before and after the marketing campaign.")
    else:
        st.write("There is no significant difference in average sales before and after the marketing campaign.")


    st.write("")
    st.write("")
    
# Display the hypothesis testing results
show_hypothesis_testing()

# Load and update the dataset
df = pd.read_csv('aggregation_data.csv')
np.random.seed(42)
df['Discount Percentage'] = np.random.uniform(5, 50, len(df))
df['Profit'] = df['Discount Percentage'] * 1000
df['Quantity Sold'] = np.random.randint(1, 100, len(df))
df['Customer Lifetime Value'] = 10000 / df['Quantity Sold']
df.to_csv('updated_aggregation_data.csv', index=False)

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
    
show_regression()

np.random.seed(42)

# Generate synthetic data
n_rows = 1000
regions = ['North', 'South', 'East', 'West']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = [2022, 2023]
advertising_expenditure = np.random.uniform(1000, 10000, n_rows)
data = {
    'Region': np.random.choice(regions, n_rows),
    'Sales': np.random.randint(500, 2000, n_rows),
    'Revenue': np.random.randint(1000, 5000, n_rows),
    'Month': np.random.choice(months, n_rows),
    'Year': np.random.choice(years, n_rows),
    'Advertising_Expenditure': advertising_expenditure,
    'Product_Category': np.random.choice(['Category_1', 'Category_2', 'Category_3'], n_rows),
    'Marketing_Campaign': np.random.choice(['Before', 'After'], n_rows)
}

df = pd.DataFrame(data)

# Save the dataset to CSV
df.to_csv('categorical_data.csv', index=False)

def show_categorical_test():
    st.header("Categorical Test")
    st.markdown("""
    Categorical data analysis often involves assessing relationships between different categorical variables. 
    Cross-tabulation is a method to quantitatively analyze the relationship between multiple variables, and 
    the chi-square test is used to determine if there is a significant association between the variables.
    """)

    # Load the dataset
    df = pd.read_csv('aggregation_data.csv')
    
    # Cross-tabulation between 'Region' and 'Product_Category'
    st.subheader("Conduct chi-square test between Region and Marketing Channels. ")
    marketing_channels = ['TV', 'Social Media', 'Email', 'Advertisement Billboards', 'Radio', 'Print Media', 'Online Ads', 'Influencer Marketing', 'Direct Mail', 'Event Sponsorship']
    df['Marketing Channels'] = np.random.choice(marketing_channels, size=len(df))
    df.to_csv('updated_aggregation_data.csv', index=False)
    contingency_table = pd.crosstab(df['Region'], df['Marketing Channels'])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    st.write("Chi-Square Test Results")
    st.write(f"Chi-Square statistic: {chi2}")
    st.write(f"p-value: {p}")
    st.write(f"Degrees of freedom: {dof}")
    st.write("Expected frequencies:")
    st.dataframe(pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns), use_container_width=True)

show_categorical_test()
