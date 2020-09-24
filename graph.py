import requests
import datetime
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import matplotlib.pyplot
import seaborn as sns

plt.style.use('seaborn')
sns.set(font='Franklin Gothic Book',
        rc={
 'axes.axisbelow':False,
 'axes.edgecolor':'lightgrey',
 'axes.facecolor': 'None',
 'axes.grid': False,
 'axes.labelcolor': 'dimgrey',
 'axes.spines.right': False,
 'axes.spines.top': False,
 'figure.facecolor': 'white',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'text.color': 'dimgrey',
 'xtick.bottom':False,
 'xtick.color':'dimgrey',
 'xtick.direction': 'out',
 'xtick.top': False,
 'ytick.color': 'dimgrey',
 'ytick.direction': 'out',
 'ytick.left': False,
 'ytick.right': False, 
        })
sns.set_context("notebook",
rc={"font.size":16,"axes.titlesize":20,"axes.labelsize":18})
def crypto(name,val=[],dal=[]):
        for i in range(15):
            start_date = datetime.datetime.now() - datetime.timedelta(i)
            a= str(start_date.year)
            b = str(start_date.month)
            c = str(start_date.day-1)
            p = str(c+"-"+b+"-"+a)   
            dal.append(p)
            apicrypto = "https://api.coingecko.com/api/v3/coins/"+name+"/history?date="+p+"&localization=false"
            data= requests.get(apicrypto).json()
            c_data=data["market_data"]["current_price"]["usd"]
            val.append(c_data)
        plt.subplots(facecolor=(.0, .0, .0))
        plt.tick_params(labelcolor='tab:cyan')
        plt.plot_date(dal,val,'xkcd:coral', linestyle='solid')
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        matplotlib.pyplot.savefig('plot.png')
        plt.show()
        
crypto()
