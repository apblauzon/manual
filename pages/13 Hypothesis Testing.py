import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats

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

    # Example 2: Determine if there is a significant difference in Revenue between two product categories
    st.subheader("Determine if There is a Significant Difference in Revenue Between Two Product Categories")
    st.write("Output:")
    # Select two product categories for comparison
    category_1 = df[df['Product_Category'] == 'Category_1']['Revenue']
    category_2 = df[df['Product_Category'] == 'Category_2']['Revenue']
    
    # Perform t-test
    t_stat_cat, p_value_cat = stats.ttest_ind(category_1, category_2)
    
    st.write(f"T-Statistic for Product Categories: {t_stat_cat:.4f}")
    st.write(f"P-Value for Product Categories: {p_value_cat:.4f}")
    
    if p_value_cat < 0.05:
        st.write("There is a significant difference in revenue between the two product categories.")
    else:
        st.write("There is no significant difference in revenue between the two product categories.")

# Display the hypothesis testing results
show_hypothesis_testing()
