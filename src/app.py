import streamlit as st
from backend import data_manipulation as dm
from backend import data_viz as dv

@st.cache(allow_output_mutation=True)
def upload_file(file):
    return dm.DataFrameHandler(file)

def data_snapshot(dh):
    dataSnapshot = st.container()

    try:
        with dataSnapshot:
            #Need to fix ugly table width: plotly table is a viable option
            st.write("Data Snapshot")
            st.dataframe(dh.df.head(5))

            st.write("Descriptive Statistics")
            st.dataframe(dh.df.describe())

            col1, col2 = st.columns(2)
            col2.write("Categorical Statistics")
            col2.table(dh.df.describe(include=['object']))

            col1.write("Missing Value Statistics")
            col1.dataframe(dh.df.isna().sum())
    except:
        pass

def data_viz_shell(dh):
    viz_type = st.selectbox("What type of visualization do you want?",
                    ('Histogram', 'Scatterplot', 'Bar Graph', 'Line Graph', 'Box Plot', 'Correlation Heatmap'))
    try:
        if viz_type != "Correlation Heatmap":
            col1, col2 = st.columns([2, 5])
            with col1:
                inputs = dataviz_inputs(filehandler, viz_type)
            with col2:
                vh = dv.VizHandler(filehandler.df, **inputs)
                st.plotly_chart(vh.plot())
        else:
            vh = dv.VizHandler(filehandler.df, viz_type=viz_type)
            st.plotly_chart(vh.plot())
    except:
        st.write("Data cannot be visualized")


def dataviz_inputs(dh, viz_type):
    
    inputs = dict()

    dataVizOptions = st.container()
    
    with dataVizOptions:
        
        inputs['viz_type'] = viz_type
        inputs['hue'] = None

        if viz_type == "Histogram" or viz_type == "Box Plot":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select a column", dh.get_numeric_columns())
                inputs['hue'] = st.selectbox("Select a column to color by", [None] + dh.get_categorical_columns())
            else:
                inputs['x'] = st.selectbox("Select a column", dh.get_numeric_columns())
            
            if viz_type == "Histogram":
                inputs['bins'] = st.slider("Number of bins", min_value=1, max_value=100, value=10)
            else:    
                inputs['log_x'] = st.checkbox("Logarithmic x-axis")
        
        elif viz_type == "Scatterplot" or viz_type == "Line Graph":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs['hue'] += st.selectbox("Select a column to color by", [None] + dh.get_categorical_columns())
            else:
                inputs['x'] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
            if viz_type == "Scatterplot":
                inputs['opacity'] = st.slider("Opacity", min_value=0.0, max_value=1.0, value=0.7)
        
        elif viz_type == "Bar Graph":
            if dh.get_categorical_columns():
                inputs['x'] = st.selectbox("Select X-axis", dh.get_categorical_columns())
                inputs['y'] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs['func'] = st.selectbox("Select a function", ('count', 'sum', 'avg', 'median'))
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
        
        st.write("## What do you want to do with your data?")
        actionMenu = st.container()

        with actionMenu:
            opt = st.radio("Choose an action:", ('Data Visualization', 'Statistics'))
            if opt == "Data Visualization":
                data_viz_shell(filehandler)
            elif opt == "Statistics":
                datastat(filehandler)
                st.write("Coming soon!")