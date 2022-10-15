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
        fig.add_trace(go.Scatter(x=plotdata.index, y = hosps))
        fig.update_layout(title='Flu Trajectory',xaxis_title='Date',yaxis_title='Hospitilization')
        # add location name to the left top of the plot
        last5dates = plotdata.index[-5:]
        last5hosps = hosps[-5:]
        # dynamic add 5 arrows to the plot
        down = 0
        for i in range(5):
            fig.add_annotation(
                x=last5dates[i],
                y=last5hosps[i],
                xref="x",
                yref="y",
                text=str(last5hosps[i]),
                # add marker to the point               
                # show arrow
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-30 if down == 0 else 30
            )
            down = 1 if down == 0 else 0
        # fig width and height
        fig.update_layout(width=1200, height=600)
        self.fig = fig
        
        return fig
            


    def plotoutState(self):
        import matplotlib.pyplot as plt
        fd = self.io.getForecastDate()
        # save the image
        self.fig.write_html("./{:s}/{:s}_{:s}_trajectory.html".format(fd,fd,self.io.locAbbr))
        self.fig.write_image("./{:s}/{:s}_{:s}_trajectory.png".format(fd,fd,self.io.locAbbr))
if __name__ == "__main__":

    pass

    

