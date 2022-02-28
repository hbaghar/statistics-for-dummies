from xml.etree.ElementInclude import include
import plotly.express as px
class VizHandler():

    def __init__(self, data, **kwargs):
        # Todo:
        # - Initialize all matplotlib figure params to set figure size, templates etc
        self.data = data
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def plot(self):
        if self.viz_type == 'Histogram': 
            return px.histogram(self.data, x = self.x, color = self.hue, nbins = self.bins, barmode='overlay')
        elif self.viz_type ==  'Scatterplot': 
            return px.scatter(self.data, x = self.x, y = self.y, color = self.hue, opacity=self.opacity)
        elif self.viz_type == 'Bar Graph':
            return px.histogram(self.data, x = self.x, y = self.y, color = self.hue, opacity=self.opacity, histfunc=self.func)
        elif self.viz_type == 'Line Graph':
            return px.line(self.data, x = self.x, y = self.y, color = self.hue)
        elif self.viz_type == 'Box Plot':
            return px.box(self.data, x = self.x, y = self.y, color = self.hue)
        elif self.viz_type == 'Correlation Heatmap':
            return px.imshow(self.data.corr())
        else:
            return None

    def rejection_region_plot(self):
        pass