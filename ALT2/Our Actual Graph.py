# Cleaning Data
# ALT2
# by Daniel, Kacper & Anthony
# 07-04-2025

import pandas as p
import numpy as np
import matplotlib.pyplot as pyplot

#These are our Libraries, which we will use throughout

df=p.read_csv('covid_worldwide.csv')

df=df.drop_duplicates()

replacements={'©':'e','§':'c','Ã':'',',':''}

#These replacements are for any countries with glitched symbols

for symbol, replacement in replacements.items():
    df['Country']=df['Country'].str.replace(symbol,replacement)
    
df['Country']=df['Country'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
df['Total Deaths']=df['Total Deaths'].str.replace(',', '', regex=True)
# df['Total Cases']=df['Total Cases'].str.replace(',', '', regex=True)
# df['Population']=df['Population'].str.replace(',', '', regex=True)
    
#Now our code is clean!!!

streamlinedDF=df[['Serial Number','Country','Total Cases','Total Deaths','Population']]

usefulDF=streamlinedDF.dropna()

Caselist = usefulDF['Total Cases']
Deathlist = usefulDF['Total Deaths']
Poplist = usefulDF['Population']
CountryList = usefulDF['Country']

#Converting everything to floats so it plots

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

#Now we get averages

Mean = float(TotalCase//TotalDeath)
Ratiolist = []
for i in range(0, 221):
    Ratiolist.append(round(FloatCase[i]/FloatDeath[i],2))
Ratiolist.sort()
Median = Ratiolist[222//2]
print("Our mean is:", Mean)
print("Our median is:", Median)

#Graphing

for y in range(0, 221):
    pyplot.scatter(FloatDeath[y], FloatCase[y], s=(FloatPop[y])/300000, alpha=0.5)
    pyplot.annotate(CountryList[y], (FloatDeath[y], FloatCase[y]), va='center', ha='center', fontsize=6)
pyplot.xlabel('Deaths')
pyplot.ylabel('Cases')
pyplot.show()