# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# question 1
#print(data.describe())
#print(data.info())

# question 2
#print("min = ",data.flow.min())
#print("max = ",data.flow.max())
#print("mean = ",data.flow.mean())
#print("std = ",data.flow.std())
#print("quartiles:\n",data.flow.quantile([0,0.25,0.5,0.75]))

# %%

# question 3
#for i in range (1,13):
#    mo = data[data.month == i]
#    print("month = ",i)
#    print("min = ",mo.flow.min())
#    print("max = ",mo.flow.max())
#    print("mean = ",mo.flow.mean())
#    print("std = ",mo.flow.std())
#    print("quartiles:\n",mo.flow.quantile([0,0.25,0.5,0.75]))
#    print("\n")


# %%
# question 4

#data.nsmallest(5,"flow",keep = "all")
#data.nlargest(5,"flow",keep = "all")
# %%
# question 5

#for i in range(1,13):
#    mo = data[data.month == i]
#    print("month = ",i)
#    print("lowest")
#    print(mo.nsmallest(1,"flow",keep = "all"))
#    print("highest")
#    print(mo.nlargest(1,"flow",keep = "all"))

#%%
# question 6
# one week forecast is 52 --> 10% range is 46.8 to 57.2

checkforecast = data[(data.flow >= 46.8) & (data.flow <= 57.2)]
datelist = checkforecast.datetime.tolist()
print(datelist)



# %%
# get averages for forecasting

wk1 = data[(data.month == 8) & (data.day >= 24) & (data.day <= 30)]
wk1mean = wk1.flow.mean()

wk2 = data[((data.month == 8) & (data.day == 31)) | ((data.month==9) & (data.day >= 1) & (data.day <= 6))]
wk2mean = wk2.flow.mean()

wk3 = data[(data.month == 9) & (data.day >= 7) & (data.day <= 13)]
wk3mean = wk3.flow.mean()

wk4 = data[(data.month == 9) & (data.day >= 14) & (data.day <= 20)]
wk4mean = wk4.flow.mean()

wk5 = data[(data.month == 9) & (data.day >= 21) & (data.day <= 27)]
wk5mean = wk5.flow.mean()

wk6 = data[((data.month == 9) & (data.day >= 28) & (data.day <= 30)) | ((data.month == 10) & (data.month >= 1) & (data.month <= 4))]
wk6mean = wk6.flow.mean()

wk7 = data[(data.month == 10) & (data.day >= 5) & (data.day <= 11)]
wk7mean = wk7.flow.mean()

wk8 = data[(data.month == 10) & (data.day >= 12) & (data.day <= 18)]
wk8mean = wk8.flow.mean()

wk9 = data[(data.month == 10) & (data.day >= 19) & (data.day <= 25)]
wk9mean = wk9.flow.mean()

wk10 = data[((data.month == 10) & (data.day >= 26) & (data.day <= 31)) | ((data.month ==11) & (data.day == 1))]
wk10mean = wk10.flow.mean()

wk11 = data[(data.month == 11) & (data.day >= 2) & (data.day <= 8)]
wk11mean = wk11.flow.mean()

wk12 = data[(data.month == 11) & (data.day >= 9) & (data.day <= 15)]
wk12mean = wk12.flow.mean()

wk13 = data[(data.month == 11) & (data.day >= 16) & (data.day <= 22)]
wk13mean = wk13.flow.mean()

wk14 = data[(data.month == 11) & (data.day >= 23) & (data.day <= 29)]
wk14mean = wk14.flow.mean()

wk15 = data[((data.month == 11) & (data.day == 30)) | ((data.month == 12) & (data.day >= 1) & (data.day <= 6))]
wk15mean = wk15.flow.mean()

wk16 = data[(data.month == 12) & (data.day >= 7) & (data.day <= 13)]
wk16mean = wk16.flow.mean()

forecasts = np.array([wk1mean,wk2mean,wk3mean,wk4mean,wk5mean,wk6mean,wk7mean,wk8mean,wk9mean,wk10mean,wk11mean,wk12mean,wk13mean,wk14mean,wk15mean,wk16mean])
print(forecasts)


# %%
