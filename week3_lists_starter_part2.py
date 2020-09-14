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
filename = 'streamflow_week3.txt'
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
# print(min(flow))
# print(max(flow))
# print(np.mean(flow))
# print(np.std(flow))

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
        if month[i] == 9 and day[i] >= 14 and day[i] <= 20:
                week4list.append(flow[i])
        elif month[i] == 9 and day[i] >= 21 and day[i] <= 27:
                week5list.append(flow[i])


prediction1week = np.mean(week4list)
prediction2week = np.mean(week5list)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(prediction1week)
print(prediction2week)

# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
# ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
#print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
# subset = [flow[j] for j in ilist]
# %%
# How many times was the daily flow greater than your prediction in the month of September 
# (express your answer in terms of the total number of times and as a percentage)?

week2prediction = 166.70552995391705
week3prediction = 197.0603686635945
week4prediction = 158.10230414746545
week5prediction = 198.9304147465438
week6prediction = 129.55898617511522

week1list = []
week2list = []
week3list = []
week4list = []
week5list = []
week6list = []

for l in range(len(flow)):
        if month[l] == 9 and day[l] >= 1 and day[l] <= 6 and year[l] <= 2000:
                week2list.append(flow[l])
        elif month[l] == 9 and day[l] >= 7 and day[l] <= 13 and year[l] <= 2000:
                week3list.append(flow[l])
        elif month[l] == 9 and day[l] >= 14 and day[l] <= 20 and year[l] <= 2000:
                week4list.append(flow[l])
        elif month[l] == 9 and day[l] >= 21 and day[l] <= 27 and year[l] <= 2000:
                week5list.append(flow[l])
        elif month[l] == 9 and day[l] >= 28 and day[l] <= 30 and year[l] <= 2000:
                week6list.append(flow[l])


count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for j in range(len(week2list)):
        if week2prediction < week2list[j]:
                count1 = count1 + 1

for k in range(len(week3list)):
        if week3prediction < week3list[k]:
                count2 = count2 + 1

for m in range(len(week4list)):
        if week4prediction < week4list[m]:
                count3 = count3 + 1

for n in range(len(week5list)):
        if week5prediction < week5list[n]:
                count4 = count4 + 1

for o in range(len(week6list)):
        if week6prediction < week6list[o]:
                count5 = count5 + 1

count = count1 + count2 + count3 + count4 + count5
tot = len(week2list) + len(week3list) + len(week4list) + len(week5list) + len(week6list)
print(count)
print(count/tot)


# %%
