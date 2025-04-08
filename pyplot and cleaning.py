# Cleaning Data
# ALT2
# by Daniel and Anthony
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

Caselist = usefulDF['Total Cases']
Deathlist = usefulDF['Total Deaths']

FloatCase = []
for i in Caselist:
    FloatCase.append(float(i))
FloatDeath = []
for i in Deathlist:
    FloatDeath.append(float(i))


#Graphing

import numpy as np
import matplotlib.pyplot as pyplot
for y in range(0, 150):
    pyplot.scatter(FloatDeath[y], FloatCase[y], s=1, alpha=0.5)
pyplot.show()
