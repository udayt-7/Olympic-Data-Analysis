import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

dm = pd.read_csv("athlete_events.csv")
#print(dm)
#Filling missing values of Age, Height and Weight by calculating mean of theier respective coloumns

mis_col = ['Age', 'Height', 'Weight']
for col in mis_col:
	dm[col] = dm[col].fillna(np.mean(dm[col]))
	dm[col] = np.round(dm[col],0)

#print(dm)

#Dropping all data of players who haven't won any medal

a1 = dm.dropna(subset=['Medal'])

#Creating 3 seperate csv files after filtering and cleaning data as 
###refined database, summer olympic db, winter olympic db

a1.to_csv("rd1.csv", index = False)
df = pd.read_csv('rd1.csv')	
#print(df)

a2 = df[df['Season']=='Summer']
a2.to_csv("summer.csv",index = False)
# ds = pd.read_csv('summer.csv')
#print(ds)

a3 = df[df['Season']=='Winter']
a3.to_csv('winter.csv', index = False)
# dw = pd.read_csv('winter.csv')
#print(dw)


#Print all missing values in the dataset

#print(df.isnull().sum())
#print(sns.heatmap(df.isnull(), cbar= False))




def medalbysports():

	#Country with most no of medals in a specific sport
	# top = df.groupby(['Sport','NOC'], as_index = True)['Sport'].agg({'Medal':'count'}).sort_values(['Medal'], ascending = False)
	# print(top)
	######find unique######
	#top = df.groupby(['Sport','NOC'], as_index = True).agg({'Medal':'count'}).sort_values(['Medal'], ascending = False)
	#print(top)

	#top1 = top.groupby(['Sport','NOC','Medal'], as_index = True).agg({'Sport':'unique'})
	#top.get_group('Swimming')
	# ds.loc[:,'Sport'].unique()
	
	#NOC and Team Duplicates

	#print(df.loc[:,['NOC','Team']].drop_duplicates()['NOC'].value_counts().head())

	##Question -- medal stats for each Sport

	cmedals = df.groupby('Sport', as_index = True).agg({'Medal':'count'})
	#print(cmedals.sort_values('Medal',ascending = False))

	#which country has most no of medals

	a= df.groupby(['NOC'], as_index = True).agg({'Medal':'count'})
	maxmedals = a.sort_values(['Medal'], ascending = False)

	#grouping medals by sport

	b = df.groupby(['Sport','NOC'], as_index = True).agg({'Medal':'count'})
	medalbysport = b.sort_values(['Sport','Medal'], ascending = False)

	#top 10 countries with most no of medals

	t = df.groupby(['Sport'], as_index = True).agg({'Medal':'count'})
	top10 = t.sort_values('Medal', ascending=False).head(10)

	print(maxmedals)
	#print(medalbysport)
	#print(top10)

	
#medalbysports()


def sportevents():

	#No of events for each Game
	#summer
	yearsplit = ds.sort_values(['Year','Season'],ascending = False)
	z = yearsplit[['Sport','Event']]
	eventsplit = z.groupby(['Sport'], as_index = True).agg({'Event':'nunique'}).sort_values('Event',ascending =False)
	#print(eventsplit.head(10))

	#top medal winning countries in last 25 years 
	yearsplit = df[df['Year'].between(1990,2016, inclusive = True)].sort_values(['Year','Season'],ascending = False)
	top25c = yearsplit.groupby(['NOC'], as_index = True).agg({'Medal':'count'}).sort_values('Medal', ascending = False).head(10)
	#print(top25c)

#sportevents()



def medal_by_age():

	#Medal Distribution graph

	medals = df
	#medals.head()
	medals = medals[np.isfinite(medals['Age'])]

	plt.figure(figsize=(20,10))
	plt.tight_layout()
	sns.countplot(medals['Age'])
	plt.title('Medal distribution')
	plt.show()

	#medals won before/after/at that particular age
	#print(df['ID'][df['Age']==26].count())

#medal_by_age()


def gender_ratio():

	gender = df.groupby(['Sex','Year']).Sport.agg(['count'])
	gender.sort_values('Year', ascending = False)
	f_count = gender.loc['F']
	m_count = gender.loc['M']
	print(f_count)
	print(m_count)

#gender_ratio()


if __name__ == '__main__':

	#medalbysports()
	#sportsevents()
	medal_by_age()
	#gender_ratio()