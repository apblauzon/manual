import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
# Load the dataset
st.set_page_config(page_title="DatViz Ai | Scatter Plot", page_icon="logo.svg")
df = pd.read_csv('retail_marketing_2.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df['MonthYear'] = df['Date'].dt.to_period('M')
monthly_data = df.groupby('MonthYear').agg({'Quantity': 'sum', 'Amount': 'sum'}).reset_index()





def show_scatterplot():
    st.header("Scatter Plots")
    st.markdown("""
    Scatter plots are useful for visualizing the relationship between two variables. You can use them to see how one metric might influence another.
    """)


    
    avg_price = df.groupby('Date')['Price'].mean().reset_index()
    total_amount = df.groupby('Date')['Amount'].sum().reset_index()
    merged_df = pd.merge(avg_price, total_amount, on='Date')

    fig = px.scatter(merged_df, x='Price', y='Amount', title='Scatterplot of Average Price vs Total Amount',
                    labels={
                        'Price': 'Average Price',
                        'Amount': 'Total Amount'
                    })
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.write("")
    st.write("**PROMPT: Generate a scatterplot of average price and total amount.**")
    st.plotly_chart(fig, use_container_width=True)   
    
    
    
    
    
    
    
    
    
    
    
    
    
# Display the scatter plots
show_scatterplot()