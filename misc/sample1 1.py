import pandas as pd
import numpy as np

df=pd.read_csv('dataset.csv')	
'''
print("first five rows")
print(df.head()) #by default prints first five rows
print("last five rows")
print(df.tail()) #by default prints lastfive rows

print("number of rows and columns")
print(df.shape) #gives number of rows and columns

male=df["Sex"]=='M'
female=df["Sex"]=='F'
print("male")
print(df[male].head())
print("female")
print(df[female].head())
'''
#print(df["Event"])
'''
events=df.Event.unique()
year=df.Year.unique()
age=df.Age.unique()
team=df.Team.unique()
city=df.City.unique()
sports=df.Sport.unique()

year=sorted(year)
age=sorted(age)

print(events)
print("\n")
print((year))
print("\n")
print(age)
print("\n")
print(team)
print("\n")
print(city)
print("\n")
print(sports)
'''
#print((df[["Medal"]]=='NA').sum())
#d=df.groupby(["Season"])
#print(d)
#print(d.groupby(["Season"].groups["Summer"]))

#print(df.corr())
#name=df.Name.unique()
#print(name)
#print(type(name))
summer=df[df["Season"]=='Summer']
print(type(summer))
male_summer_players=summer.Name.unique()
print(type(male_summer_players))
#a=str(male_summer_players)
#np.savetxt("summer.csv",a,delimiter=",")
x=male_summer_players.reshape((116122,1))
with open("summer.csv","w") as f:
	for i in x:
		np.savetxt(f,i)
