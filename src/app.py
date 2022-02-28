import streamlit as st
import pandas as pd
from backend import data_manipulation as dm
from backend import data_viz as dv

@st.cache(allow_output_mutation=True)
def upload_file(file):
    return dm.DataFrameHandler(file)

def data_snapshot(dh):
    dataSnapshot = st.container()

    with dataSnapshot:
        #Need to fix ugly table width: plotly table is a viable option
        st.write("Data Snapshot")
        st.table(dh.df.head(5))

        st.write("Descriptive Statistics")
        st.table(dh.get_descriptive_stats())

        st.write("Categorical Statistics")
        st.table(dh.get_categorial_stats())

        st.write("Missing Value Statistics")
        st.table(dh.get_missing_value_stats())


def data_options(dh):
    actionMenu = st.container()

    with actionMenu:
        st.write("What do you want to do?")
        data_option = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
        return data_option


def dataviz(dh, viz_type):
    
    keys = ['viz_type', 'x', 'y', 'bins', 'hue', 'func']
    inputs = dict.fromkeys(keys)

    dataVizOptions = st.container()
    
    with dataVizOptions:
        
        inputs['viz_type'] = viz_type

        if viz_type == "Histogram" or viz_type == "Box Plot":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select a column", dh.get_numeric_columns())
                inputs['hue'] = st.selectbox("Select a column to color by", [None] + dh.get_categorical_columns())
            else:
                inputs['x'] = st.selectbox("Select a column", dh.get_numeric_columns())
            
            if viz_type == "Histogram":
                inputs['bins'] = st.slider("Number of bins", min_value=1, max_value=100, value=10)
        
        elif viz_type == "Scatterplot" or viz_type == "Line Graph":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs['hue'] = st.selectbox("Select a column to color by", [None] + dh.get_categorical_columns())
            else:
                inputs['x'] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
        
        elif viz_type == "Bar Graph":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select X-axis", dh.get_categorical_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs['func'] = st.selectbox("Select a function", ('count', 'sum', 'mean', 'median'))
                inputs['hue'] = st.selectbox("Select a column to color by", [None] + dh.get_categorical_columns())
            else:
                st.write("No categorical columns found in dataset")
        
        else:
            pass
    
    return inputs


def datastat(dh):
    return st.radio("What type of hypothesis test do you want?",
                    ('Z-Test', 'T-Test', 'ANOVA'))


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)
    uploaded_file = st.file_uploader("Select a file", type=['csv', 'xls', 'xlsx', 'json'])
    filehandler = None
    if uploaded_file:
        filehandler = upload_file(uploaded_file)
        data_snapshot(filehandler)
        option = data_options(filehandler)
        if option == "Data Visualization":
            viz_type = st.selectbox("What type of visualization do you want?",
                    ('Histogram', 'Scatterplot', 'Bar Graph', 'Line Graph', 'Box Plot', 'Correlation Matrix'))
            col1, col2 = st.columns([1,2])
            with col1:
                inputs = dataviz(filehandler, viz_type)
                st.write(inputs)
            with col2:
                vh = dv.VizHandler(filehandler.df, **inputs)
                st.pyplot(vh.fig, vh.plot())
        elif  option == "Statistics":
            inputs = datastat(filehandler)
            st.write(inputs)