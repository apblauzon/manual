import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import plotly.express as px
# Load the dataset
df = pd.read_csv('new_data.csv')


def show_correlation_matrix():
    st.header("Correlation Matrix / Heatmap")
    st.markdown("""
    A correlation matrix is useful for understanding the relationships between multiple variables. It shows how strongly pairs of variables are related, which can help in identifying patterns and dependencies in your data.
    """)

   # Calculate correlation matrix for numerical variables excluding 'lat', 'lon' and 'CustomerID'
    corr_matrix = df[['Quantity', 'Price', 'DiscountApplied', 'TotalAmount']].corr()

    # Create a heatmap using Plotly
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect='auto',
        color_continuous_scale='blues',
        title='Correlation Matrix of Numerical Variables',
        labels={'color': 'Correlation'},
    )

    fig.update_layout(
        annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))]
    )

    st.plotly_chart(fig, use_container_width=True)

# Display the correlation matrix
show_correlation_matrix()