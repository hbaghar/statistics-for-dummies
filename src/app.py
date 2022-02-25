import imp
import streamlit as st
import pandas as pd
from backend import data_manipulation as dm

def upload_file():
    uploaded_file = st.file_uploader("Select a file", type=['csv', 'xls', 'xlsx', 'json'])
    if uploaded_file:
        file_handler = dm.DataFrameHandler(uploaded_file)
        st.table(file_handler.df.head(10))
        data_options()


def data_options():
    st.write("What do you want to do?")
    data_option = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
    if data_option == 'Data Visualization':
        viz_option = dataviz()
        st.write("--Call into Data Visualization Class with ", viz_option, "Visualization Type")
    if data_option == 'Statistics':
        stat_option = datastat()
        st.write("--Call Statistics Class with ", stat_option, "Test Type")


def dataviz():
    return st.radio("What type of visualization do you want?",
                    ('Histogram', 'Scatterplot', 'Bar Graph', 'Line Graph', 'Rejection Region Plot'))


def datastat():
    return st.radio("What type of hypothesis test do you want?",
                    ('Z-Test', 'T-Test', 'ANOVA'))


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)
    upload_file()