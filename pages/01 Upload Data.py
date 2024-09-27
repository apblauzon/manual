
import streamlit as st
import pandas as pd

def show_uploading_data():
    st.header("Uploading Your Data File")
    st.markdown("""
    1. **Ensure Your Data is Clean**: Remove missing values, typographical errors, and superfluous characters. Address outliers outside of DatViz AI, if necessary, then re-upload your data.
    2. **Use Only One Header**: Your data should have a single, clear header.
    3. **Column and Row Organization**: Columns represent variables, and rows represent observations.
    4. **Name Columns Properly**: Use short, meaningful names for each column.
    5. **Column Name Sensitivity**: DatViz AI is not strictly column name and character sensitive, but it is advisable to use the exact names from your header.
    6. **Geomapping Columns**: Ensure Latitude (Lat) and Longitude (Lon) columns are present. Subscribers can use our R-Shiny app "Geolo" to calculate these from addresses.
    """)

show_uploading_data()
