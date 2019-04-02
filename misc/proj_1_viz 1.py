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
ds = pd.read_csv('summer.csv')
#print(ds)

a3 = df[df['Season']=='Winter']
a3.to_csv('winter.csv', index = False)
dw = pd.read_csv('winter.csv')
#print(dw)

def null_heatmap():
	#Print all missing values in the dataset

	#print(df.isnull().sum())
	#sns.heatmap(dm.isnull(), cbar= False)

#null_heatmap()

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

def participants():

	x = df.groupby('Year')['ID'].count()
	population=pd.DataFrame({'Year':x.index,'player_count':x.values})
	objects = population['Year']
	y_pos = np.arange(len(objects))
	performance=population['player_count']
	plt.figure(figsize=(15, 4))
	plt.bar(y_pos, performance, align = 'center',alpha= 1)
	plt.xticks(y_pos, objects,rotation=90)
	plt.ylabel('Participants')
	plt.xlabel('year')
	plt.title('Partcipants by year')
	plt.show()

#participants()

if __name__ == '__main__':

	null_heatmap()
	#medal_by_age()
	#gender_ratio()
	#participants()
	