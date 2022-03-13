import plotly.express as px


class VizHandler:
    """
    Class for handling visualization of data. We accept inputs in the form of a dictionary of keyword arguments as each visualiztion type has different arguments.

    Parameters
    ----------
    data : pandas.DataFrame
        Data to be visualized.
    viz_type : str
        Type of visualization to be used.
    x : str
        Column name of x-axis.
    y : str
        Column name of y-axis.
    hue : str
        Column name of hue (variable to use as color for data points).
    bins : int
        Number of bins to use for histogram.
    log_x : bool
        Whether to use logarithmic scale for x-axis.
    opacity : float
        Opacity of data points.
    func : str
        Function to use for bar graph.
    """

    def __init__(self, data, **kwargs):
        # Todo:
        # - Initialize all matplotlib figure params to set figure size, templates etc
        self.data = data
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def plot(self):
        """
        Plot data. Written in a manner so as to be able to call a single function called plot() in app.py thereby simplifying the UI code.
        """

        if self.viz_type == "Histogram":
            return px.histogram(
                self.data, x=self.x, color=self.hue, nbins=self.bins, barmode="overlay"
            )
        elif self.viz_type == "Scatterplot":
            return px.scatter(
                self.data, x=self.x, y=self.y, color=self.hue, opacity=self.opacity
            )
        elif self.viz_type == "Bar Graph":
            return px.histogram(
                self.data, x=self.x, y=self.y, color=self.hue, histfunc=self.func
            )
        elif self.viz_type == "Line Graph":
            return px.line(self.data, x=self.x, y=self.y, color=self.hue)
        elif self.viz_type == "Box Plot":
            return px.box(self.data, x=self.x, color=self.hue, log_x=self.log_x)
        elif self.viz_type == "Correlation Heatmap":
            return px.imshow(self.data.corr())
        else:
            return None

    def rejection_region_plot(self):
        pass
