import unittest
from backend.data_manipulation import DataFrameHandler
from backend.data_viz import VizHandler
from io import BytesIO
import streamlit as st

class TestVizHandler(unittest.TestCase):

    def test_histogram(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Histogram"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = None
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "histogram")

    def test_scatter(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Scatterplot"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "scatter")

    def test_bar(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Bar Graph"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "histogram")

    def test_line(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Line Graph"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "scatter")

    def test_box(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Box Plot"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "box")

    def test_heatmap(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "Correlation Heatmap"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig.to_dict()["data"][0]["type"], "heatmap")

    def test_null(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["data"] = df_obj.df
        inputs["viz_type"] = "lol idek"
        inputs["x"] = "PetalLengthCm"
        inputs["y"] = "PetalWidthCm"
        inputs["hue"] = "PetalLengthCm"
        inputs["bins"] = 5
        inputs["log_x"] = 0
        inputs["opacity"] = 0.5
        inputs["func"] = None

        # Make viz object
        viz_obj = VizHandler(data_handler=df_obj.df, **inputs)

        # Create plotly obj
        fig = viz_obj.plot()

        # unit testing time
        self.assertEqual(fig, None)

class TestVizHandler(unittest.TestCase):
    pass
if __name__ == '__main__':
    unittest.main()