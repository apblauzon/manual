import pandas as pd
import numpy as np
import streamlit as st
from scipy.stats import chi2_contingency
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
    df = pd.read_csv('categorical_data.csv')

    # Cross-tabulation between 'Region' and 'Product_Category'
    st.subheader("Generate Cross Tabulation: Region vs. Product Category")
    cross_tab = pd.crosstab(df['Region'], df['Product_Category'])
    st.write(cross_tab)
    
    # Chi-Square Test
    st.subheader("Conduct Chi-Square Test between Region and Cateogory")
    st.write("Output:")
    chi2, p, dof, ex = chi2_contingency(cross_tab)
    
    st.write(f"Chi-Square Statistic: {chi2}")
    st.write(f"P-Value: {p}")
    st.write(f"Degrees of Freedom: {dof}")
    st.write("Expected Frequencies Table:")
    st.write(pd.DataFrame(ex, index=cross_tab.index, columns=cross_tab.columns))

    # Interpretation
    if p < 0.05:
        st.write("The result is significant at p < 0.05, suggesting a significant association between Region and Product Category.")
    else:
        st.write("The result is not significant at p < 0.05, suggesting no significant association between Region and Product Category.")

# Display the categorical test results
show_categorical_test()
