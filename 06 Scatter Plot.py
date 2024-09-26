import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
# Load the dataset

df = pd.read_csv('new_data.csv')

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%d/%m/%Y')
df['MonthYear'] = df['TransactionDate'].dt.to_period('M')
monthly_data = df.groupby('MonthYear').agg({'Quantity': 'sum', 'TotalAmount': 'sum'}).reset_index()





def show_scatterplot():
    st.header("Scatter Plots")
    st.markdown("""
    Scatter plots are useful for visualizing the relationship between two variables. You can use them to see how one metric might influence another.
    """)

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
    st.plotly_chart(fig, use_container_width=True)
    
    avg_price = df.groupby('TransactionDate')['Price'].mean().reset_index()
    total_amount = df.groupby('TransactionDate')['TotalAmount'].sum().reset_index()
    merged_df = pd.merge(avg_price, total_amount, on='TransactionDate')

    fig = px.scatter(merged_df, x='Price', y='TotalAmount', title='Scatterplot of Average Price vs Total Amount',
                    labels={
                        'Price': 'Average Price',
                        'TotalAmount': 'Total Amount'
                    })
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.plotly_chart(fig, use_container_width=True)   
    
    
    
    
    
    
    
    
    
    
    
    
    
# Display the scatter plots
show_scatterplot()