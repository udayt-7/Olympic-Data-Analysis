import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def function_year(year):
  ds = pd.read_csv('summer.csv')

  #mapping city to host countries  
  city_to_country = {'Mexico City':'Mexico' ,
                     'Berlin':'Germany',
                     'Munich':'Germany',
                     'Garmisch-Partenkirchen':'Germany',
                     'Montreal':'Canada',
                     'Calgary':'Canada',
                     'Vancouver':'Canada',
                     'Stockholm':'Sweden',
                     'Moskva':'Russia',
                     'Sochi':'Russia',
                     'St. Louis':'United States',
                     'Lake Placid':'United States',
                     'Los Angeles':'United States',
                     'Atlanta':'United States',
                     'Squaw Valley':'United States',
                     'Salt Lake City':'United States',
                     'Seoul':'South Korea' ,
                     'Barcelona':'Spain' ,
                     'Helsinki':'Finland',
                     'Innsbruck':'Austria' ,
                     'Melbourne':'Australia',
                     'Sydney':'Australia',
                     'Athina':'Greece' ,
                     'Beijing':'China' ,
                     'Antwerpen':'Belgium',
                     "Cortina d'Ampezzo":'Italy',
                     'Roma':'Italy',
                     'Torino':'Italy',
                     'London':'UK',
                     'Amsterdam':'Netherlands',
                     'Tokyo':'Japan',
                     'Sapporo':'Japan',
                     'Nagano':'Japan',
                     'Oslo':'Norway',
                     'Lillehammer':'Norway',
                     'Sarajevo':'Yugoslavia' ,
                     'Sankt Moritz':'Switzerland',
                     'Paris':'France',
                     'Chamonix':'France',
                     'Albertville':'France',
                     'Grenoble':'France',
                     'Rio de Janeiro':'Brazil'}

  #Replacing Old values of country with latest value
  ds['Team'].replace(
      to_replace='Soviet Union',
      value='Russia',
      inplace=True
  )

  ds['Team'].replace(
      to_replace='Great Britain',
      value='UK',
      inplace=True
  )


  ds["Country_Host"]=ds["City"].map(city_to_country)


  ds = pd.concat([ds,pd.get_dummies(ds.Medal)],axis=1)
  ds['allmedals']= ds['Bronze'] + ds['Gold'] + ds['Silver'] 


  country_data=ds.groupby(["Country_Host","City"])["Year"].unique()
  country_data=country_data.to_frame(name=None)
  #country_data

  #print(year)
  y = ds[ds.Year == year]
  

  host_city = y.iloc[0,11]
  
  n_sports = y['Sport'].nunique()
  
  n_events = y['Event'].nunique()
  
  #n_events
  n_parts = y['Name'].nunique()
  
  print("\n\nOlympics in the year",year," was conducted at",host_city, 'and' ,n_parts,'players had participated in',n_sports,"Sports and,",n_events,'Events')

  noc = y.groupby(['Team'], as_index = True).agg({'Medal':'count'})
  maxmedals = noc.sort_values(['Medal'], ascending = False)
  maxmedals = maxmedals.reset_index()
  top_c = maxmedals.head(5)
  #top_c

  # labels = top_c.Team
  # sizes = top_c.Medal
  # explode = (0.1, 0, 0, 0, 0)  
  # colors =  ['gold','silver','brown','green','teal']
  # plt.pie(sizes, explode=explode, labels=labels,colors= colors, autopct='%1.1f%%',shadow=True, startangle=90)
  # plt.axis('equal') 
  # plt.title("Countries Dominating the Given Year")
  # plt.show()

  y1 = y[['Name','Team','Medal']]
  y1 =y.groupby(['Name','Team']).agg({'Medal':'count'}).sort_values('Medal', ascending = False)
  y1 = y1.reset_index()

  top_p = y1.head(5)
  #top_p


  objects = top_p.Name
  y_pos = np.arange(len(objects))
  performance = top_p.Medal

  # plt.bar(y_pos, performance, align='center', alpha=0.5)
  # plt.xticks(y_pos, objects, rotation = 20)
  # plt.xlabel('Players')
  # plt.ylabel('Medal Count')
  # plt.title('Top 5 Athletes of Given Year')
  # plt.tight_layout()
  # plt.show()


  sr = y.groupby('Sex').agg({'Sex':'count'})
  sr = sr.rename(columns={'Sex': 'Total'})
  sr =sr.reset_index()
  #sr

  #DONUT M VS F

  # plt.pie(sr.Total, labels= ('Female','Male'), autopct = '%1.1f%%', colors=['blue','silver'], shadow= True)
  # p=plt.gcf()
  # my_circle=plt.Circle( (0,0), 0.7, color='white')
  # p.gca().add_artist(my_circle)
  # plt.title('Gender Distribution for Given Year')
  # plt.show()

  # y.head()


  # Extract year, host nation and team name from the data
  #yht = y.groupby(['Team','Country_Host','Bronze','Silver','Gold']).agg({'allmedals':'sum'}).reset_index()
  host_team = y[y.Team == y.Country_Host]


  h_name = host_team.iloc[0,15]


  h_sports = host_team['Sport'].nunique()


  h_events = host_team['Event'].nunique()

  h_t = host_team['Name'].nunique()


  # h_m = host_team[host_team.Sex == 'M']

  # h_m['Name'].nunique()


  # h_f= host_team[host_team.Sex == 'F']
  # h_f['Name'].nunique()


  h_mc = host_team['Medal'].count()

  print("\nHost Country Stats:")
  print( h_t, " players participated in ,",h_sports,"Sports,",h_events,"Events and", h_name  ,"won",h_mc,"medals")


  h_medals = host_team.groupby('Sport').agg({'Medal':'count'}).sort_values('Medal',ascending = False).reset_index()
  #h_medals = h_medals.dropna()
  #h_medals = h_medals.loc[~(h_medals==0).all(axis=)]

  #h_medalsdf=h_medals.dropna(how='all',axis=0)


  h_m = h_medals[h_medals.Medal<1]
  h_medals = h_medals.drop(h_m.index, axis =0)

  h_medals= h_medals.head(5)



  # sns.countplot(h_medals['Medal'])

  # plot1 = sns.barplot('Sport','Medal',data=h_medals).set_xticklabels(h_medals.Sport,rotation=65)

  # plt.xlabel('Sports')

  # plt.ylabel('No of Medals Won')
                    
  # plt.title('Age at which a player has won most number of Medals for the given Sport')
  # #plt.tight_layout()
  # plt.show()


  host_team = host_team[['Name','Team','Medal']]
  h_t1 =host_team.groupby(['Name','Team']).agg({'Medal':'count'}).sort_values('Medal', ascending = False)
  h_t1 = h_t1.reset_index()

  top_p = h_t1.head(5)
  #top_p


  objects = top_p.Name
  print('\n\nTop 5 players of host_team are listed below:\n')
  print(top_p)
  y_pos = np.arange(len(objects))
  performance = top_p.Medal

  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects, rotation = 90)
  plt.xlabel('Players')
  plt.ylabel('Medal Count')
  plt.title('Top 5 Athletes Host country')


  fig = plt.figure(figsize=(10,10))

  plt.subplot(2, 2, 1)

  labels = top_c.Team
  sizes = top_c.Medal
  explode = (0.1, 0, 0, 0, 0)  
  colors =  ['gold','silver','brown','green','teal']
  plt.pie(sizes, explode=explode, labels=labels,colors= colors, autopct='%1.1f%%',shadow=True, startangle=90)
  plt.axis('equal') 
  plt.title("Top Countries")


  plt.subplot(2, 2, 2)

  plt.pie(sr.Total, labels= ('Female','Male'), autopct = '%1.1f%%', colors=['blue','silver'], shadow= True)
  p=plt.gcf()
  my_circle=plt.Circle( (0,0), 0.7, color='white')
  p.gca().add_artist(my_circle)
  plt.title('Gender Distribution')


  plt.subplot(2, 2, 3)
  sns.countplot(h_medals['Medal'])

  plot1 = sns.barplot('Sport','Medal',data=h_medals).set_xticklabels(h_medals.Sport,rotation=30)

  plt.xlabel('Sports')
  plt.ylabel('No of Medals Won')
  plt.title('Host Country Top Sports')


  plt.subplot(2, 2, 4)

  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects, rotation = 65)
  plt.xlabel('Players')
  plt.ylabel('Medal Count')
  plt.title('Top 5 Athletes Host country')

  fig.suptitle((host_city,year,'Analysis'))
  plt.tight_layout()
  plt.show()

if __name__=="__main__":
  function_year(int(input("Enter the year:")))
