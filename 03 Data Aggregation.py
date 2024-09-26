import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('new_data.csv')

def show_aggregations():
    st.header("Data Aggregation")
    st.markdown("""
    Aggregation involves summarizing data by combining multiple records into a single value based on a specified criterion. It helps in analyzing data at different levels, such as by region, month, or year, and is commonly used for reporting and deriving insights from large datasets.
    """)

    type_mapping = df.dtypes.astype(str).map(lambda x: 'Numerical' if x in ['int64', 'float64'] else 'Character')
    missing_values = df.isna().sum()

    # Combine type information and missing values into a DataFrame
    info_df = pd.DataFrame({'Data Type': type_mapping, 'Missing Values': missing_values}).reset_index()
    info_df.columns = ['Variable', 'Data Type', 'Missing Values']

    # Display the DataFrame in Streamlit
    st.dataframe(info_df, use_container_width=True)

# Display the aggregations
show_aggregations()
