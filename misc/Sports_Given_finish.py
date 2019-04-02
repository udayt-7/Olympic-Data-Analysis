import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def function(sports):
	df = pd.read_csv('athlete_events.csv')
	dr = pd.read_csv('rd1.csv')	
	# print(df)

	a2 = df[df['Season']=='Summer']
	a2.to_csv("summer.csv",index = False)
	ds = pd.read_csv('summer.csv')
	#print(ds)

	a3 = df[df['Season']=='Winter']
	a3.to_csv('winter.csv', index = False)
	dw = pd.read_csv('winter.csv')
	#print(dw)
	df = pd.concat([df,pd.get_dummies(df.Medal)],axis=1)
	df['allmedals']= df['Bronze'] + df['Gold'] + df['Silver'] 

	ds = pd.concat([ds,pd.get_dummies(ds.Medal)],axis=1)
	ds['allmedals']= ds['Bronze'] + ds['Gold'] + ds['Silver'] 

	s = ds[ds.Sport == sports]

	n_events = s[['Event']]
	n_events = n_events.nunique()
	n_events

	d = s.groupby('Team').agg({'Medal':'count'}).sort_values('Medal',ascending =False)
	d = d.reset_index()
	dom = d.head(5)

	##PIE CHART

	# labels = dom.Team
	# sizes = dom.Medal
	# explode = (0.1, 0, 0, 0, 0)  
	# colors =  ['gold','silver','brown','green','teal']

	# plt.pie(sizes, explode=explode, labels=labels,colors= colors, autopct='%1.1f%%',
	#         shadow=True, startangle=90)
	# plt.axis('equal') 
	# plt.title("Countries Dominating the Given Sport")
	# plt.show()


	#Average Age

	a = s[['Year', 'Age']]
	meanage = s.groupby('Year')['Age'].mean()
	meanage = pd.DataFrame({'Year':meanage.index,'Age':meanage.values})

	# plt.plot( 'Year', 'Age', data=meanage, linestyle='-', marker='o')

	# plt.xlabel("YEAR")
	# plt.ylabel("Age")
	# plt.title("Average age of a Player for the given Sport")
	# plt.show()


	# plt.figure(figsize=(12, 10))
	# ax = sns.scatterplot(x="Height", y="Weight", data=s,label = 'Height(in CM) vs Weight(in KG)', color = 'black')
	# plt.legend()
	# plt.title('Height vs Weight  for given Sport')

	medals = s.groupby('Age').agg({'Medal':'count'})
	medals = medals.reset_index()

	# sns.countplot(medals['Age'])
	# plot1 = sns.barplot('Age','Medal',data=medals).set_xticklabels(medals.Age,rotation=82)
	# plt.xlabel('Age of a Player')
	# plt.ylabel('No of Medals Won')
	# plt.title('Age at which a player has won most number of Medals for the given Sport')

	# fig = plt.figure()

	plt.subplot(2, 2, 1)

	labels = dom.Team
	sizes = dom.Medal
	explode = (0.1, 0, 0, 0, 0)  
	colors =  ['gold','silver','brown','green','teal']
	plt.pie(sizes, explode=explode, labels=labels,colors= colors, autopct='%1.1f%%',shadow=True, startangle=90)
	plt.axis('equal') 
	plt.title("Countries Dominating the Given Sport")



	plt.subplot(2, 2, 2)


	ax = sns.scatterplot(x="Height", y="Weight", data=s,label = 'Height(in CM) vs Weight(in KG)', color = 'black')
	plt.legend()
	plt.title('Height vs Weight  for given Sport')

	plt.subplot(2, 2, 3)

	plt.plot( 'Year', 'Age', data=meanage, linestyle='-', marker='o',label = 'Avg_Age of Player')

	plt.xlabel("YEAR")
	plt.ylabel("Age")
	plt.legend()
	plt.title("Average age of a Player for the given Sport")


	plt.subplot(2, 2, 4)

	sns.countplot(medals['Age'])
	plot1 = sns.barplot('Age','Medal',data=medals).set_xticklabels(medals.Age,rotation=82)
	plt.xlabel('Age of a Player')
	plt.ylabel('No of Medals Won')

	plt.title('Age at which a player has won most number of Medals for the given Sport')

	plt.show()

inp=input("Enter Sport")
function(inp)