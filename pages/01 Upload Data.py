
import streamlit as st
import pandas as pd
st.set_page_config(page_title="DatViz Ai | Upload Data", page_icon="logo.svg")

def show_uploading_data():
    st.header("Uploading Your Data File")
    st.markdown("""
    1. First and foremost, if you have **sensitive information** in your dataset, we  suggest either deleting that column or using some record ID that will camouflage the data, but stilll make sense to your data visualization and analysis. 
    2. **Ensure Your Data is Clean**: Remove missing values, typographical errors, and superfluous characters. Address outliers outside of DatViz AI, if necessary, then re-upload your data.
    3. **Use Only One Header**: Your data should have a single, clear header.
    4. **Column and Row Organization**: Columns represent variables, and rows represent observations.
    5. **Name Columns Properly**: Use short, meaningful names for each column.
    6. **Column Name Sensitivity**: DatViz AI is not strictly column name and character sensitive, but it is advisable to use the exact names from your header.
    7. **Geomapping Columns**: Ensure Latitude (Lat) and Longitude (Lon) columns are present.
    """)

show_uploading_data()
