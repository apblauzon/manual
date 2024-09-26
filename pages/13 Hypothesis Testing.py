import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import scipy.stats as stats


df = pd.read_csv('new_data.csv')
# Perform the t-test
t_stat, p_val = stats.ttest_1samp(df['TotalAmount'].dropna(), popmean=0)



# Streamlit app
def show_hypothesis_testing():
    st.title("Hypothesis Testing")
    st.markdown("""
    A hypothesis test helps evaluate if a sales strategy works by analyzing a small sample of customer interactions to determine if there’s enough evidence to support the claim.
    """)

    # Display the results
    st.write(f'T-test Statistic: {t_stat:.4f}')
    st.write(f'p-value: {p_val:.4f}')

    if p_val < 0.05:
        st.write('Conclusion: The test is significant, we reject the null hypothesis.')
    else:
        st.write('Conclusion: The test is not significant, we fail to reject the null hypothesis.')
    
# Display the hypothesis testing results
show_hypothesis_testing()

