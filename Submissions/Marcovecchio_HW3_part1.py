# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

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

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(len(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
week1list = []
week2list = []
week3list = []
week4list = []
week5list = []
week6list = []
week7list = []
week8list = []
week9list = []
week10list = []
week11list = []
week12list = []
week13list = []
week14list = []
week15list = []
week16list = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if month[i] == 8 and day[i] >= 24 and day [i] <= 30:
                week1list.append(flow[i])
        elif (month[i] == 8 and day[i] == 31) or (month[i] == 9 and day[i] >= 1 and day[i] <= 6):
                week2list.append(flow[i])
        elif month[i] == 9 and day[i] >= 7 and day[i] <= 13:
                week3list.append(flow[i])
        elif month[i] == 9 and day[i] >= 14 and day[i] <= 20:
                week4list.append(flow[i])
        elif month[i] == 9 and day[i] >= 21 and day[i] <= 27:
                week5list.append(flow[i])
        elif (month[i] == 9 and day[i] >= 28 and day[i] <= 30) or (month[i] == 10 and day[i] >= 1 and day[i] <= 4):
                week6list.append(flow[i])
        elif month[i] == 10 and day[i] >= 5 and day[i] <= 11:
                week7list.append(flow[i])
        elif month[i] == 10 and day[i] >= 12 and day[i] <= 18:
                week8list.append(flow[i])
        elif month[i] == 10 and day[i] >= 19 and day[i] <= 25:
                week9list.append(flow[i])
        elif (month[i] == 10 and day[i] >= 26 and day[i] <= 31) or (month[i] == 11 and day[i] == 1):
                week10list.append(flow[i])
        elif month[i] == 11 and day[i] >= 2 and day[i] <= 8:
                week11list.append(flow[i])
        elif month[i] == 11 and day[i] >= 9 and day[i] <= 15:
                week12list.append(flow[i])
        elif month[i] == 11 and day[i] >= 16 and day[i] <= 22:
                week13list.append(flow[i])
        elif month[i] == 11 and day[i] >= 23 and day[i] <= 29:
                week14list.append(flow[i])
        elif (month[i] == 11 and day[i] == 30) or (month[i] == 12 and day[i] >= 1 and day[i] <= 6):
                week15list.append(flow[i])
        elif month[i] == 12 and day[i] >= 7 and day[i] <= 13:
                week16list.append(flow[i])

weeklist = []
weeklist.append(np.mean(week1list))
weeklist.append(np.mean(week2list))
weeklist.append(np.mean(week3list))
weeklist.append(np.mean(week4list))
weeklist.append(np.mean(week5list))
weeklist.append(np.mean(week6list))
weeklist.append(np.mean(week7list))
weeklist.append(np.mean(week8list))
weeklist.append(np.mean(week9list))
weeklist.append(np.mean(week10list))
weeklist.append(np.mean(week11list))
weeklist.append(np.mean(week12list))
weeklist.append(np.mean(week13list))
weeklist.append(np.mean(week14list))
weeklist.append(np.mean(week15list))
weeklist.append(np.mean(week16list))

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(weeklist)


# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
# ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
#print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
# subset = [flow[j] for j in ilist]
# %%

