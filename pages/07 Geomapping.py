import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_geomapping():
    st.header("Geomapping")
    st.markdown("""
    Geomapping is useful for visualizing data spatially on maps. You can use geomaps to see how different metrics are distributed across geographical locations, such as sales or profit by city or region.
    """)

    # Filter data for top 20 highest profit
    st.subheader("Generate Geomap with Top 20 Highest Profit.")
    top_20_profit = df.nlargest(20, 'Revenue')  # Changed from 'Sales' to 'Revenue' for profit
    fig_top_profit = px.scatter_geo(top_20_profit, lat='Latitude', lon='Longitude', size='Revenue', 
                                    color='Sales',  # Color by Sales
                                    color_continuous_scale='YlOrRd',  # Yellow to Red color scale
                                    projection='natural earth', 
                                    title='Top 20 Highest Profit',
                                    labels={'Revenue': 'Profit Amount', 'Sales': 'Sales Amount'},
                                    size_max=10,  # Adjust bubble size
                                    opacity=0.6,  # Adjust bubble opacity
                                    )
    fig_top_profit.update_geos(fitbounds="locations")  # Fit map to data locations
    st.plotly_chart(fig_top_profit)

    # Filter data for Region = East
    st.subheader("Generate Geomap with Sales in Region = East.")
    df_east = df[df['Region'] == 'East']
    fig_east = px.scatter_geo(df_east, lat='Latitude', lon='Longitude', size='Sales', 
                             color='Sales', 
                             color_continuous_scale='YlOrRd',  # Yellow to Red color scale
                             projection='natural earth', 
                             title='Sales Distribution in East Region',
                             labels={'Sales': 'Sales Amount'},
                             size_max=10,  # Adjust bubble size
                             opacity=0.6,  # Adjust bubble opacity
                             )
    fig_east.update_geos(fitbounds="locations")  # Fit map to data locations
    st.plotly_chart(fig_east)

# Display the geomaps
show_geomapping()
