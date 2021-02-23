'''
Michael Mirkovic
Analyazation of cases accross italy and spain, 
Attempt made to make the graph also reflect mortality 



'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
plt.rcParams['figure.figsize'] = (16,7) 
casesDF = pd.read_excel("CasesCorn.xlsx")
#errorchecking
#print("casesDF.iloc[0:1:]")

deathsDF = pd.read_excel("DeathCorn.xlsx")
#error checking
#print("deathsDF.iloc[0:1:]") 

casesItaly=casesDF.iloc[0,1:]
#print(casesItaly)
casesSpain=casesDF.iloc[1,1:]
#print(casesSpain)
#attempting to do the same thing with fatalities vs just cases 
'''
deathsItaly=deathsDF.iloc[0,1:]
#print(deathsItaly)
DeathsSpain=deathsDF.iloc[1,1:]
#print(deathsInSpain)
deathsInItaly = []
deathsInSpain = []

for x in range( 1,len(deathsItaly) -1) :
	
	if casesDF.iloc[0,x] == 0 :
		deathsInItaly.append(0)
	else:
		tempDeathsInItaly = deathsDF.iloc[0,x]/casesDF.iloc[0,x]
		deathsInItaly.append(tempDeathsInItaly)

	if casesDF.iloc[1,x] == 0 :
		deathsInSpain.append(0)
	else:
		tempDeathsInSpain = deathsDF.iloc[1,x]/casesDF.iloc[1,x]
		deathsInSpain.append(tempDeathsInSpain)
print(deathsInItaly)
print(deathsInSpain)
'''

plt.suptitle('Italy Versus Spain' , fontsize = 18)
plt.xlabel('Date', fontsize =14)
plt.ylabel('cases', fontsize =14)
plt.plot(casesDF.columns[1:],casesItaly,'-',color ='red')
plt.plot(casesDF.columns[1:],casesSpain,'-', color ='blue')
plt.xticks(rotation = 'vertical' , size = 12)
plt.legend(['Italy','Spain'], fontsize= 14)
plt.show()
