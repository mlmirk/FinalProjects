'''
Michael Mirkovic
Analyazation of US, EU, and Global stockmarkets 



'''
import pandas as pd 
import matplotlib
from matplotlib import pyplot as plt 
plt.rcParams['figure.figsize'] = (16,7) 
#widen the grapgh so it is not so its eaiser to interpet 
matplotlib.use('Qt5Agg')
stockData = pd.read_excel('StockMarket.xlsx')
#import data
SP = stockData[stockData.Category =='SP']
GlobalDow= stockData[stockData.Category =='GlobalDow']
STOXXEurope= stockData[stockData.Category =='STOXXEurope']
plt.plot(SP.Date, SP.Close , color = 'blue' , linewidth = 3)
plt.plot(GlobalDow.Date, GlobalDow.Close , color = 'red' , linewidth = 3)
plt.plot(STOXXEurope.Date, STOXXEurope.Close , color = 'green' , linewidth = 3)
plt.title('EU Vs. USA Vs. Global markets' , fontsize = 20)
plt.legend(['USA - S&P' , 'Europe - STOXXEurope' , ' Global - GlobalDow'])
plt.xlabel('Date' , fontsize  = 12)
plt.ylabel('Category' , fontsize = 12)
plt.show()