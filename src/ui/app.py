import streamlit as st
import pandas as pd


def upload_file():
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        data_options()


def data_options():
    st.write("What do you want to do?")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        data_manip = st.button('Data Manipulation')
    with col2:
        data_viz = st.button('Data Visualization')
    with col3:
        data_stats = st.button('Statistics')
    if data_manip:
        st.write("--Call into Data Manipulation Class--")
    if data_viz:
        st.write("--Call into Data Visualization Class--")
    if data_stats:
        st.write("--Call Statistics Class--")


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)
    upload_file()