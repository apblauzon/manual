import pandas as pd
import numpy as np
import streamlit as st
from scipy.stats import chi2_contingency
import scipy.stats as stats
import plotly.express as px

# Generate or load the dataset
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

# Streamlit app
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
      
    st.write("")
    st.write("")
    
    st.subheader("Conduct chi-square test between Marketing Campaign and Marketing Channels. ")
    contingency_table = pd.crosstab(df['Marketing_Campaign'], df['Marketing Channels'])
    chi2, p, dof, ex = stats.chi2_contingency(contingency_table)
    st.write(f"Chi-square Test Statistic: {chi2}")
    st.write(f"P-value: {p}")
    st.write(f"Degrees of Freedom: {dof}")
    fig = px.imshow(contingency_table, text_auto=True, aspect="auto")
    fig.update_layout(title="Contingency Table: Marketing Campaign vs Marketing Channels", annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)


show_categorical_test()
