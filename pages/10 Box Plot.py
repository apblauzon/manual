import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_box_plot():
    st.subheader("Box Plot (Box and Whiskers)")
    st.markdown("""
    Box plots are useful for showing the distribution of data and identifying outliers. They are helpful for comparing distributions across different categories, such as sales or revenue by region or month.
    """)

    # Box Plot of Sales by Region
    st.subheader("Generate Box Plot of Sales by Region.")
    fig_sales_region = px.box(df, x='Region', y='Sales',
                              title='Box Plot of Sales by Region',
                              labels={'Sales': 'Sales Amount'})
    st.plotly_chart(fig_sales_region)

    # st.write("")
    # st.write("")
    
    # # Box Plot of Revenue by Month
    # st.subheader("Generate Box Plot of Revenue by Month.")
    # month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
    # fig = px.box(df, x='Month', y='Revenue', category_orders={"Month": month_order}, title="Box Plot of Revenue by Month")
    # fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    # st.plotly_chart(fig, use_container_width=True)


# Display the box plots
show_box_plot()
