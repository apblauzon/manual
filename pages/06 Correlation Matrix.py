import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_correlation_matrix():
    st.header("Correlation Matrix")
    st.markdown("""
    A correlation matrix is useful for understanding the relationships between multiple variables. It shows how strongly pairs of variables are related, which can help in identifying patterns and dependencies in your data.
    """)

    # Select numerical columns for correlation matrix
    numerical_columns = ['Sales', 'Revenue', 'Orders']  # Include 'Cost' and 'Profit' if they exist in the dataset
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
