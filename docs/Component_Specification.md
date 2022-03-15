# Component Specification

We will describe all the components that make up the project. The project consists of one application module that handles all the front end and multiple back end modules that handle different abstractions and functionalities.

## **Application module (app.py)**

The application module handles all concerns regarding the frontend. For this project, we decided to use Streamlit, which easily allows us to turn data scripts into shareable web apps using Python. It creates an interactive GUI on the web and it is all created and launched using the Streamlit library in Python. We chose Streamlit given its ease of use and low requirement on the frontend details for user interface design, it has very deep modules that take many of the frontend decisions, allowing users to fastly create the interface without need of much code. 

As mentioned before, this application module handles all concerns with regards to the frontend and interaction with the GUI, it is the only module that calls Streamlit methods and interacts with Streamlit. Hence, this module is the bridge between the backend and the GUI. Specifically, this module allows us to respond to every interaction that the user has with our GUI, from uploading a file, showing the data snapshot, obtaining the user's inputs and outputting the corresponding visualizations or statistical test results. In this current version, it offers the following functions:

> *upload_file*: Accepts a file and returns a DataFrameHandler object. Written in order to leverage Streamlit's caching functionality.

> *data_snapshot*: Providing a snapshot of the dataframe - descriptive, categorical, missing values stats and header of dataframe.

> *data_viz_shell*: Function that reserves space for results of data visualization. Collects the inputs from the input function, calls the visualization handler and presents the results.

> *dataviz_inputs*: Function that collects the user inputs for data visualization

> *datastat_shell*: Function that reserves space for results of statistical tests

> *datastat_inputs*: Function that collects the user inputs for statistical tests.

## **DataFrameHandler class (data_manipulation.py)**

The DataFrameHandler class requires a UploadedFile object (Streamlit file object that extends BytesIO) that will be a CSV, XLSX or JSON (restriction of file type to upload is handled in the frontend) for instantiation. The class converts this incoming file into a handable DataFrame object and allows multiple data manipulation functions that are required in many places of our application. In this current version, it offers the following functions:

> *get_numeric_columns*: Returns list with names of the numeric columns in the dataframe

> *get_categorical_columns*: Returns list with names of the categorical columns in the dataframe. There can be numeric columns that are categorical, we will assume that more than 10 unique values is the threshold between categorical and numeric features

> *get_column_categories*: Returns unique list of column categories. 

> *get_descriptive_stats*: Returns the descriptive statistics of numeric columns of the dataframe 

> *get_categorical_stats*: Returns the descriptive statistics of categorical columns of the dataframe 

> *get_missing_value_stats*: Returns a string with the amount of missing values in each column inside the dataframe

> *slice_by_column*: Returns dictionary with Series objects from the numeric_column each sliced by their respective grouping in the categorical_column.If there are NaN in the categorical_column we don't consider them.

## **VizHandler class (data_viz.py)**

The VizHandler class handles the visualization of the data, meaning that it is in charge of plotting graphs according to inputs received in the parameters (*kwargs). This class is easily extensible and allows to plot multiple plots by just needing to instantiate one object with the necessary parameters for that specific plot using keyword arguments. In this current version, it offers the following function:

> *plot*: Plot data. Written in a manner so as to be able to call a single function called plot() in app.py thereby simplifying the UI code. It currently can plot histograms, scatterplots, bar-graphs, line-graphs, box-plots and correlation heatmaps. 

## **Hypothesis Test Handler module (hypothesis_test_handler.py)**

This module creates a HypothesisTests class (parent class) that creates a hypothesis test object. This class is created given that there are clear similarities between the HypothesisTests parameters and methods such as pvalue, test_type, test_statistic and performing a test. All hypothesis tests (TTest, ZTest and ANOVA) inherit from this parent class. The class receives the specific inputs and creates an appropriate instantiation of the hypothesis test function with the parameters specified. In this current version, it offers the following function:

> *perform_test*: Thoughtful method that allows code readability and significant line reduction in the application module given that all the test is performed in only one line of code. 

## **Hypothesis Test module (hypothesis_tests.py)**

In this module we have all of our hypothesis test code. It contains multiple functions that perform the different array of possibilities of hypothesis tests that the user might want to perform when using our application. In this current version, it offers the following functions:

> *t_test_1_samp*: One sample T-test

> *t_test_welch*: Two sample T-test (unequal variance)

> *t_test_2_sampl_equal_var*: Two sample T-test (equal variance)

> *z_test_1_samp*: One sample Z-test

> *z_test_2_samp*: Two sample Z-test

> *one_way_ANOVA*: One way ANOVA (F-test)
