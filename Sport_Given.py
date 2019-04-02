import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys



def function_sports(sport):
	ds = pd.read_csv('summer.csv')
	ds['Team'].replace(to_replace='Soviet Union',value='Russia',inplace=True)
	ds['Team'].replace(to_replace='Great Britain',value='UK',inplace=True)
	

	ds = pd.concat([ds,pd.get_dummies(ds.Medal)],axis=1)
	ds['allmedals']= ds['Bronze'] + ds['Gold'] + ds['Silver'] 

	s = ds[ds.Sport == sport]

	n_events = s[['Event']]
	n_events = n_events.nunique()
	#print(sport ,"has",n_events,"events")

	d = s.groupby('Team').agg({'Medal':'count'}).sort_values('Medal',ascending =False)
	d = d.reset_index()
	dom = d.head(5)
	#dom

	#Top 5 counties of that sport
	##Donut

	# size_of_groups= dom.Medal
	# names = dom.Team 
	# # Create a pieplot
	# plt.pie(size_of_groups)
	# plt.pie(size_of_groups, labels=names, autopct = '%1.1f%%', colors=['red','yellow','green','black','blue'])
	# p=plt.gcf()
	# p.set_size_inches(7, 9)
	# my_circle=plt.Circle( (0,0), 0.7, color='white')
	# p.gca().add_artist(my_circle)
	# plt.show()

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
	#meanage.set_index('Year', inplace = True)

	# sns.set(rc={'figure.figsize':(18,12)})
	# plot1 = sns.barplot('Year','Age',data=meanage).set_xticklabels(meanage.Year,rotation=82)
	# #plot1.set(xlabel='YEAR',ylabel='Number of people')
	# plt.xlabel("YEAR")
	# plt.ylabel("Age")
	# plt.title("Average age of a Player for the given Sport")



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

	ti = sport
	print(ti)

	fig = plt.figure(figsize=(20.5,12))

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
	plt.xticks(range(1896,2020,4), rotation = 60)
	plt.legend()
	plt.title("Average age of a Player for the given Sport")


	plt.subplot(2, 2, 4)

	sns.countplot(medals['Age'])
	plot1 = sns.barplot('Age','Medal',data=medals).set_xticklabels(medals.Age,rotation=82)
	plt.xlabel('Age of a Player')
	plt.ylabel('No of Medals Won')

	plt.title('Age at which a player has won most number of Medals for the given Sport')

	#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.2)
	#fig.suptitle(sport)
	plt.show()

if __name__=="__main__":
	function_sports(input("Enter the sport:"))