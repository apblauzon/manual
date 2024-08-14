import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('aggregation_data.csv')
np.random.seed(42)
df['Discount Percentage'] = np.random.uniform(5, 50, len(df))
df['Profit'] = df['Discount Percentage'] * 1000
df['Quantity Sold'] = np.random.randint(1, 100, len(df))
df['Customer Lifetime Value'] = 10000 / df['Quantity Sold']
df.to_csv('updated_aggregation_data.csv', index=False)

def show_correlation_matrix():
    st.header("Correlation Matrix")
    st.markdown("""
    A correlation matrix is useful for understanding the relationships between multiple variables. It shows how strongly pairs of variables are related, which can help in identifying patterns and dependencies in your data.
    """)

    # Select numerical columns for correlation matrix
    numerical_columns = ['Sales', 'Revenue', 'Orders','Profit','Quantity Sold','Customer Lifetime Value','Discount Percentage']  # Include 'Cost' and 'Profit' if they exist in the dataset
    df_numerical = df[numerical_columns]

    # Compute the correlation matrix
    correlation_matrix = df_numerical.corr()

    # Create a heatmap of the correlation matrix
    fig = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns.tolist(),
        y=correlation_matrix.columns.tolist(),
        annotation_text=correlation_matrix.round(2).values,
        colorscale='Viridis',
        showscale=True
    )
    
    st.plotly_chart(fig)

# Display the correlation matrix
show_correlation_matrix()
