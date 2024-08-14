import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_heat_map():
    st.subheader("Heat Map")
    st.markdown("""
    **Sample Prompts for Heat Map**:
    - "Generate Heat Map of Correlation Matrix."
    - "Generate Heat Map of Sales by Region and Month."

    **Description**:
    Heat maps are useful for visualizing data intensity or frequency across two dimensions. They are ideal for displaying patterns and correlations in data matrices.
    """)

    # Heat Map of Correlation Matrix
    st.subheader("Generate Heat Map of Correlation Matrix.")
    numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
    corr_matrix = numeric_df.corr()  # Compute correlation matrix
    fig_corr_heatmap = px.imshow(corr_matrix, 
                                text_auto=True, 
                                title='Correlation Matrix Heat Map',
                                labels=dict(color='Correlation Coefficient'),
                                color_continuous_scale='YlGnBu')  # Choose color scale
    st.plotly_chart(fig_corr_heatmap)

    # Heat Map of Sales by Region and Month
    st.subheader("Generate Heat Map of Sales by Region and Month.")
    sales_by_region_month = df.groupby(['Region', 'Month'])['Sales'].sum().unstack()
    fig_sales_heatmap = px.imshow(sales_by_region_month, 
                                 text_auto=True, 
                                 title='Sales by Region and Month Heat Map',
                                 labels=dict(color='Total Sales'),
                                 color_continuous_scale='YlOrRd')  # Choose color scale
    st.plotly_chart(fig_sales_heatmap)

# Display the heat maps
show_heat_map()
