
'''
Michael Mirkovic
Analyazation of cases within the US




'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Qt5Agg')
plt.rcParams['figure.figsize'] = (16,7) 
casesDF= pd.read_csv('time_series_covid19_confirmed_US.csv')

casesData = casesDF.iloc[:,50:]


confirmedList= []
for x in range(len(casesData.columns)):
	confirmed=0
	
	for y in range(len(casesData.index)):
		temp= casesData.iloc[y,x]
		confirmed += temp
	confirmedList = np.append(confirmedList,confirmed)
tempDict = {'date' : casesData.columns, 'confirmed cases' : confirmedList}
confirmedDF=pd.DataFrame(tempDict)
#print(confirmedDF)
plt.suptitle('Covid Cases in the USA', fontsize=20)
plt.xlabel('Date' , fontsize = 14)
plt.ylabel('Confirmed cases (total)' , fontsize=12)
plt.xticks(rotation = 'vertical' , size = 8)
#making the dates easier to read before this it was illegable 
plt.plot(casesData.columns,confirmedList, '-' , color ='red' , linewidth= 4 )
plt.show()
