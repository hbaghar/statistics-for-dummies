import streamlit as st

from backend import data_manipulation as dm
from backend import data_viz as dv
from backend import hypothesis_test_handler as hth


@st.cache(allow_output_mutation=True)
def upload_file(file):
    """
    Accepts a file and returns a DataFrameHandler object. Written in order to leverage streamlit's caching functionality.

    input:
        file: file object

    returns:
        DataFrameHandler object
    """
    return dm.DataFrameHandler(file)


def data_snapshot(dh):
    """
    Providing a snapshot of the dataframe - descriptive, categorical, missing values stats and header of dataframe.
    """
    dataSnapshot = st.container()

    try:
        with dataSnapshot:
            # Need to fix ugly table width: plotly table is a viable option
            st.write("Data Snapshot")
            st.dataframe(dh.df.head(5))

            st.write("Descriptive Statistics")
            st.dataframe(dh.get_descriptive_stats())

            col1, col2 = st.columns([1, 2])

            col1.write("Missing Value Statistics")
            col1.dataframe(dh.get_missing_value_stats())
            try:
                col2.write("Categorical Statistics")
                col2.dataframe(dh.get_categorical_stats())
            except Exception:
                col2.write("No categorical data")

    except Exception:
        st.write("Data cannot be visualized")
        raise Exception


def data_viz_shell(dh):
    """
    Function that reserves space for results of data visualization.

    Collects the inputs from the input function, calls the visualiztion hadler and presents the results.

    input:
        dh: DataFrameHandler object

    returns:
        None
    """
    viz_type = st.selectbox(
        "What type of visualization do you want?",
        (
            "Histogram",
            "Scatterplot",
            "Bar Graph",
            "Line Graph",
            "Box Plot",
            "Correlation Heatmap",
        ),
    )
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
    except Exception:
        st.write("Data cannot be visualized")


def dataviz_inputs(dh, viz_type):
    """
    Function that collects the user inputs for data visualization.

    input:
        dh: DataFrameHandler object
        viz_type: string mentioning the type of visualization

    returns:
        inputs: dictionary of inputs
    """

    inputs = dict()

    dataVizOptions = st.container()

    with dataVizOptions:

        inputs["viz_type"] = viz_type
        inputs["hue"] = None

        if viz_type == "Histogram" or viz_type == "Box Plot":
            if dh.get_categorical_columns():
                inputs["x"] = st.selectbox("Select a column", dh.get_numeric_columns())
                inputs["hue"] = st.selectbox(
                    "Select a column to color by", [None] + dh.get_categorical_columns()
                )
            else:
                inputs["x"] = st.selectbox("Select a column", dh.get_numeric_columns())

            if viz_type == "Histogram":
                inputs["bins"] = st.slider(
                    "Number of bins", min_value=1, max_value=100, value=10
                )
            else:
                inputs["log_x"] = st.checkbox("Logarithmic x-axis")

        elif viz_type == "Scatterplot" or viz_type == "Line Graph":
            if dh.get_categorical_columns():
                inputs["x"] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs["y"] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs["hue"] = st.selectbox(
                    "Select a column to color by", [None] + dh.get_categorical_columns()
                )
            else:
                inputs["x"] = st.selectbox("Select X-axis", dh.get_numeric_columns())
                inputs["y"] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
            if viz_type == "Scatterplot":
                inputs["opacity"] = st.slider(
                    "Opacity", min_value=0.0, max_value=1.0, value=0.7
                )

        elif viz_type == "Bar Graph":
            if dh.get_categorical_columns():
                inputs["x"] = st.selectbox(
                    "Select X-axis", dh.get_categorical_columns()
                )
                inputs["y"] = st.selectbox("Select Y-axis", dh.get_numeric_columns())
                inputs["func"] = st.selectbox(
                    "Select a function", ("count", "sum", "avg")
                )
                inputs["hue"] = st.selectbox(
                    "Select a column to color by", [None] + dh.get_categorical_columns()
                )
            else:
                st.write("No categorical columns found in dataset")

        else:
            pass

    return inputs


def datastat_shell(dh):
    """
    Function that reserves space for results of statistical tests.

    input:
        dh: DataFrameHandler object

    returns:
        None
    """
    test = st.selectbox("Select a statistical test", ("Z-Test", "T-Test", "ANOVA"))
    inputs = datastat_inputs(dh, test)

    test_obj = {"Z-Test": hth.ZTest, "T-Test": hth.TTest, "ANOVA": hth.ANOVA}
    # Add warning message for NaN values

    dataStatResults = st.container()

    with dataStatResults:
        results = test_obj[test](data_handler=dh, **inputs).perform_test()
        try:
            st.write(f"Results of {inputs['sample']} {test}:")
        except KeyError:
            st.write(f"Results of {test}:")
        # st.write(inputs)
        if results["accept"] == 0:
            st.write("Cannot reject null hypothesis")
        else:
            st.write(
                "Reject null hypothesis: true difference in means is not equal to 0"
            )
        write_dict = {
            "p_value": "p value: ",
            "z_value": "Test statistic for z: ",
            "t_value": "Test statistic for t: ",
            "f_value": "Test statistic for F: ",
        }
        if test != "ANOVA":
            if inputs["num_samples"] == "Two sample":
                write_dict["sample_mean_1"] = f'Sample mean for {inputs["cat1"]}: '
                write_dict["sample_mean_2"] = f'Sample mean for {inputs["cat2"]}: '
                if results["cat_NaN_found"] or results["num_NaN_found"]:
                    st.warning(
                        "Missing values were found, these were exculded while conducting statistical tests"
                    )
            else:
                write_dict[
                    "sample_mean_1"
                ] = f'Sample mean for {inputs["numeric_col"]}: '
                if results["num_NaN_found"]:
                    st.warning(
                        "Missing values were found, these were exculded while conducting statistical tests"
                    )
            st.write(
                "Confidence interval: ",
                (round(results["con_low"], 3), round(results["con_up"], 3)),
            )
        # st.write(results)
        for key, value in results.items():
            if key in write_dict.keys():
                st.write(write_dict[key], round(value, 3))


def datastat_inputs(dh, test):
    """
    Function that collects the user inputs for statistical tests.

    input:
        dh: DataFrameHandler object
        test: string mentioning the type of statistical test

    returns:
        inputs: dictionary of inputs
    """
    inputs = dict()
    dataStatOptions = st.container()

    with dataStatOptions:

        if test == "Z-Test" or test == "T-Test":
            sample = st.radio("Select a test type", ("One sample", "Two sample"))
            inputs["num_samples"] = sample
            if sample == "One sample":
                inputs["numeric_col"] = st.selectbox(
                    "Select a column", dh.get_numeric_columns()
                )
                inputs["mu"] = st.number_input("Enter population mean", value=0.0)
            else:
                if test == "T-Test":
                    inputs["equal_var"] = st.checkbox("Equal variance")

                inputs["numeric_col"] = st.selectbox(
                    "Select numeric column", dh.get_numeric_columns()
                )
                inputs["cat"] = st.selectbox(
                    "Select categorical column", dh.get_categorical_columns()
                )

                if inputs["cat"]:
                    col1, col2 = st.columns(2)
                    inputs["cat1"] = col1.selectbox(
                        "Select category 1", dh.get_column_categories(inputs["cat"])
                    )
                    inputs["cat2"] = col2.selectbox(
                        "Select category 2", dh.get_column_categories(inputs["cat"])
                    )

        elif test == "ANOVA":
            inputs["numeric_col"] = st.selectbox(
                "Select numeric column", dh.get_numeric_columns()
            )
            inputs["cat"] = st.selectbox(
                "Select categorical column", dh.get_categorical_columns()
            )

        else:
            pass
        inputs["significance_level"] = st.number_input(
            "Enter the significance level", value=0.05
        )

        return inputs


if __name__ == "__main__":
    """
    Main function that runs the app.
    """
    st.write(
        """
    # DATA 515 Project - Statistics for Dummies
    """
    )
    uploaded_file = st.file_uploader("Select a file", type=["csv", "xlsx", "json"])
    filehandler = None
    if uploaded_file:
        filehandler = upload_file(uploaded_file)
        data_snapshot(filehandler)

        st.write("## What do you want to do with your data?")
        actionMenu = st.container()

        with actionMenu:
            opt = st.radio("Choose an action:", ("Data Visualization", "Statistics"))
            if opt == "Data Visualization":
                data_viz_shell(filehandler)
            elif opt == "Statistics":
                datastat_shell(filehandler)
