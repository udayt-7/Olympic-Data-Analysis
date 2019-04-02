import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def avg_age():

	ds = pd.read_csv('summer.csv')
	#print(ds)

	y1 = ds[ds.Year==2000]
	y2 = ds[ds.Year==2004]
	y3 = ds[ds.Year==2008]
	y4 = ds[ds.Year==2012]
	y5 = ds[ds.Year==2016]
	
	choice = int(input("Select the year which you want to check the average age of:\n 1.2000\n2.2004\n3.2008\n4.2012\n5.2016"))
	
	if choice == 1 or choice ==2000:
		
		aage = y1.groupby(['Year','Sport']).agg({'Age':'mean'})
		

	if choice == 2 or choice ==2004:
		
		aage = y2.groupby(['Year','Sport']).agg({'Age':'mean'})

	if choice == 3 or choice ==2008:
		
		aage = y3.groupby(['Year','Sport']).agg({'Age':'mean'})

	if choice == 4 or choice ==2012:
		
		aage = y4.groupby(['Year','Sport']).agg({'Age':'mean'})

	if choice == 5 or choice ==2016:
		
		aage = y5.groupby(['Year','Sport']).agg({'Age':'mean'})




    