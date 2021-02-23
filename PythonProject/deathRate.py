'''
Michael Mirkovic
Analyazation of cases accross Usa reflecting motrality rather then 
number of cases  



'''
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Qt5Agg')
plt.rcParams['figure.figsize'] = (16,7) 
casesDF = pd.read_csv('time_series_covid19_confirmed_US.csv')
deathsDF = pd.read_csv('time_series_covid19_deaths_US.csv')
confirmedCases = casesDF.iloc[:,50:]
confirmedDeaths = deathsDF.iloc[:,51:]

fatalities = []
deathList = [] 
for col in range(len(confirmedCases.columns)):
		cases = 0
		deaths = 0

		for row in range(len(confirmedCases.index)):
			casesTemp = confirmedCases.iloc[row,col]
			cases += casesTemp
			deathTemp = confirmedDeaths.iloc[row,col]
			deaths += deathTemp
		fatalityRate = deaths/cases
		deathList= np.append(deathList,deaths)
		fatalities = np.append(fatalities, fatalityRate)
tempDict = {'date' : confirmedCases.columns, 'death': deathList , 'fatality' : fatalityRate}
fatalityDF= pd.DataFrame(tempDict)
#print(fatalityDF)
#createing a dataframe that is easier to manipulate then an entire spreadsheet 

plt.suptitle('Fatality Rate in the USA' , fontsize = 20)
plt.xlabel('Dates' , fontsize = 16)
plt.ylabel('Fatality Rate' , fontsize= 16)
plt.plot(casesDF.columns[50:], fatalities, '-' ,color = 'red')
plt.legend(['U.S.'], fontsize = 15)
plt.xticks(rotation = 'vertical' , size = 8)
plt.show()