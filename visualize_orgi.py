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
        def plotlyTrajectory(self):
            import plotly.graph_objects as go
            import plotly.express as px
            import pandas as pd

            plotdata = self.dataWide
            hosps = plotdata[self.locname].values
            dates = plotdata.index[::-1][::4][::-1]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=hosps[::-1][::4][::-1],mode='lines+markers',name='lines+markers'))
            fig.update_layout(title='Flu Trajectory',xaxis_title='Date',yaxis_title='Hospitilization')
            # add location name to the left top of the plot
            fig.add_annotation(
                x=0.05,
                y=0.95,
                xref="paper",
                yref="paper",
                text=self.locname,
                showarrow=False
            )
            self.fig = fig
            return fig
            
            # fig.add_annotation(x=dates, y=hosps[::-1][::4][::-1],text=hosps[::-1][::4][::-1],showarrow=True,arrowhead=7,ax=0,ay=-40)
    def fluTrajectory_new(self):
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.style.use("fivethirtyeight")
        fig,ax = plt.subplots()

        plotdata = self.dataWide
        hosps = plotdata[self.locname].values
        dates = plotdata.index[::-1][::4][::-1]
        print(self.locname,plotdata.shape)
        ax.plot( plotdata, lw=2,alpha=0.40,color="blue" )
        ax.scatter(dates,hosps[::-1][::4][::-1],s=10,color="blue",alpha=0.8)
        
        #label points 5 weeks in the past
        hospsPast5 = hosps[-5:]
        datesPast5 = plotdata.index[-5:]

        ax.scatter(datesPast5,hospsPast5,s=10,color="blue",alpha=0.8)
        offset = 5
        # change the date format to INT
        yoffset=0
        for date,hosp in zip(datesPast5,hospsPast5): 
            # change the str to date
            date1 = datetime.datetime.strptime(date,"%Y-%m-%d")
            # add one day to the date and keep it ad YYYY-MM-DD
            datenext = date1 + datetime.timedelta(days=1)
            # transfrom the date to YYYY-MM-DD
            datenext = datenext.strftime("%Y-%m-%d")
            # print("nextdate",date,datenext)
            ax.annotate(
                int(hosp),
                xy=(date,hosp),
                # change the string format to INT
                xytext=(datenext, hosp+yoffset),    # fraction, fraction
                arrowprops=dict(arrowstyle='->',color='black',connectionstyle='arc3'),
                fontsize=5,
            )  
            # yoffset+=0.1
            # text=ax.text(date,hosp-offset,s="{:d}".format(int(hosp))
            #         ,ha="left",va="top",fontsize=5)
                    #,bbox = dict(facecolor=mpl.rcParams['axes.facecolor'], alpha=0.4)   )

        ax.tick_params(which="both", labelsize=6)

        ax.set_ylabel("Number of weekly\nconfirmed hospitlizations due to influenza", fontsize=6)
        ax.set_xlabel("",fontsize=6)

        ax.set_xticks(ax.get_xticks()[::-1][::10][::-1])
        ax.set_yticklabels(["{:,}".format(int(y)) for y in ax.get_yticks()])
        
        ax.text(0.01,0.95,"{:s}".format(self.locname[0]),fontsize=6,fontweight="bold",ha="left",va="top",transform=ax.transAxes)
        ax.text(0.01,0.80,"Data source = https://github.com/cdcepi/Flusight-forecast-data",fontsize=6,ha="left",va="top",transform=ax.transAxes)

        self.ax=ax
        self.fig=fig
        return fig,ax

    def mm2inch(x):
        return x/25.4
    
    def plotoutBanner(self):
        import matplotlib.pyplot as plt

        plt.subplots_adjust(bottom=0.115)
        self.fig.set_size_inches( 1600/300, 300/300 )
        plt.savefig("{:s}_UStrajectory.jpg".format(self.io.getForecastDate()),dpi=300)

    def plotoutState(self):
        import matplotlib.pyplot as plt

        plt.subplots_adjust(bottom=0.115)
        self.fig.set_size_inches( 1600/300, 800/300 )

        fd = self.io.getForecastDate()
        plt.savefig("./{:s}/{:s}_{:s}trajectory.jpg".format(fd,fd,self.io.locAbbr),dpi=300)

if __name__ == "__main__":

    pass

    

