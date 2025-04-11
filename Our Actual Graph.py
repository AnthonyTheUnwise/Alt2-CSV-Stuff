# Cleaning Data
# ALT2
# by Daniel, Kacper & Anthony
# 07-04-2025

import pandas as p
#import matplotlib as m

df=p.read_csv('covid_worldwide.csv')

print(df)

df=df.drop_duplicates()

replacements={'©':'e','§':'c','Ã':'',',':''} # Reunion, Curacao

for symbol, replacement in replacements.items():
    df['Country']=df['Country'].str.replace(symbol,replacement)
    
df['Country']=df['Country'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
df['Total Deaths']=df['Total Deaths'].str.replace(',', '', regex=True)
    
#df.to_csv('output2.csv',index=False)

streamlinedDF=df[['Serial Number','Country','Total Cases','Total Deaths','Population']]

usefulDF=streamlinedDF.dropna()
print(usefulDF)

Caselist = usefulDF['Total Cases']
Deathlist = usefulDF['Total Deaths']
Poplist = usefulDF['Population']
CountryList = usefulDF['Country']

FloatCase = []
for i in Caselist:
    FloatCase.append(float(i))
FloatDeath = []
for i in Deathlist:
    FloatDeath.append(float(i))
FloatPop = []
for i in Poplist:
    FloatPop.append(float(i))
TotalCase = 0
for i in FloatCase:
    TotalCase = TotalCase + i
TotalDeath = 0
for i in FloatDeath:
    TotalDeath = TotalDeath + i
Mean = float(TotalCase//TotalDeath)
Ratiolist = []
for i in range(0, 221):
    Ratiolist.append(round(FloatCase[i]/FloatDeath[i],2))
Ratiolist.sort()
Median = Ratiolist[222//2]
print("Our mean is:", Mean)
print("Our median is:", Median)


#Graphing

import numpy as np
import matplotlib.pyplot as pyplot
for y in range(0, 221):
    pyplot.scatter(FloatDeath[y], FloatCase[y], s=(FloatPop[y])/300000, alpha=0.5)
    pyplot.annotate(CountryList[y], (FloatDeath[y], FloatCase[y]), va='center', ha='center', fontsize=6)
pyplot.xlabel('Deaths')
pyplot.ylabel('Cases')
pyplot.show()
