#mcandrew
import datetime

from matplotlib.pyplot import arrow
# from adjustText import adjust_text

class visualize(object):
    def __init__(self,io):
        self.io = io
        self.dataLong, self.dataWide = io.locData__long, io.locData__wide
        self.locname = io.locname
    def fluTrajectory(self):
        # use plotly to plot out the trajectory
        import plotly.graph_objects as go
        import plotly.express as px
        import pandas as pd

        plotdata = self.dataWide
        hosps = plotdata[self.locname].values
        hosps = hosps.reshape(-1)
        dates = plotdata.index[::-1][::4][::-1]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=plotdata.index, y=hosps[::-1][::4][::-1],mode='lines+markers',name='lines+markers'))
        fig.update_layout(title='Flu Trajectory',xaxis_title='Date',yaxis_title='Hospitilization')
        # add location name to the left top of the plot
        fig.add_annotation(
            x=0.05,
            y=0.95,
            xref="paper",
            yref="paper",
            text=self.locname[0],
            showarrow=False
        )
        self.fig = fig
        return fig
            


    def plotoutState(self):
        import matplotlib.pyplot as plt


        fd = self.io.getForecastDate()
        # save the image
        self.fig.write_html("./{:s}/{:s}_{:s}trajectory.html".format(fd,fd,self.io.locAbbr))
if __name__ == "__main__":

    pass

    

