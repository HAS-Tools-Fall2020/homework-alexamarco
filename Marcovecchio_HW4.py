# Starter code for Homework 4

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

# Make a numpy zeros
# of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)



# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7

# columns: 0=year, 1=month, 2=day, 3=flow

#flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))

# this gives a list of T/F where the criteria are met
#(flow_data[:,3] > 600) & (flow_data[:,1]==7)

# this give the flow values where that criteria is met
#flow_pick = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 3]

# this give the year values where that criteria is met
#year_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 0]

# this give the all rows  where that criteria is met
#all_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), ]

# Calculate the average flow for these same criteria 
#flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

#print("Flow meets this critera", flow_count, " times")
#print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
#mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
#plt.hist(flow_data[:,3], bins = mybins)
#plt.title('Streamflow')
#plt.xlabel('Flow [cfs]')
#plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
#flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
#print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
#flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
#print('Method two flow quantiles:', flow_quants2[:,3])


# %%
# print(flow_data)
# columns: 0=year, 1=month, 2=day, 3=flow
arr_shape = flow_data.shape
rows = arr_shape[0]
columns = arr_shape[1]
#print(rows)

ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0
ct7 = 0
ct8 = 0
ct9 = 0
ct10 = 0
ct11 = 0
ct12 = 0
ct13 = 0
ct14 = 0
ct15 = 0
ct16 = 0

for i in range(rows-1):
        if flow_data[i,1] == 8 and flow_data[i,2] >= 24 and flow_data[i,2] <= 30:
                ct1 = ct1 + 1
        elif (flow_data[i,1] == 8 and flow_data[i,2] == 31) or (flow_data[i,1] == 9 and flow_data[i,2] >= 1 and flow_data[i,2] <= 6):
                ct2 = ct2 + 1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 7 and flow_data[i,2] <= 13:
                ct3 = ct3 + 1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 14 and flow_data[i,2] <= 20:
                ct4 = ct4 + 1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 21 and flow_data[i,2] <= 27:
                ct5 = ct5 + 1
        elif (flow_data[i,1] == 9 and flow_data[i,2] >= 28 and flow_data[i,2] <= 30) or (flow_data[i,1] == 10 and flow_data[i,2] >= 1 and flow_data[i,2] <= 4):
                ct6 = ct6 + 1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 5 and flow_data[i,2] <= 11:
                ct7 = ct7 + 1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 12 and flow_data[i,2] <= 18:
                ct8 = ct8 + 1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 19 and flow_data[i,2] <= 25:
                ct9 = ct9 + 1
        elif (flow_data[i,1] == 10 and flow_data[i,2] >= 26 and flow_data[i,2] <= 31) or (flow_data[i,1] == 11 and flow_data[i,2] == 1):
                ct10 = ct10 + 1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 2 and flow_data[i,2] <= 8:
                ct11 = ct11 + 1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 9 and flow_data[i,2] <= 15:
                ct12 = ct12 + 1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 16 and flow_data[i,2] <= 22:
                ct13 = ct13 + 1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 23 and flow_data[i,2] <= 29:
                ct14 = ct14 + 1
        elif (flow_data[i,1] == 11 and flow_data[i,2] == 30) or (flow_data[i,1] == 12 and flow_data[i,2] >= 1 and flow_data[i,2] <= 6):
                ct15 = ct15 + 1
        elif flow_data[i,1] == 12 and flow_data[i,2] >= 7 and flow_data[i,2] <= 13:
                ct16 = ct16 + 1

wk1arr = np.zeros(ct1)
wk2arr = np.zeros(ct2)
wk3arr = np.zeros(ct3)
wk4arr = np.zeros(ct4)
wk5arr = np.zeros(ct5)
wk6arr = np.zeros(ct6)
wk7arr = np.zeros(ct7)
wk8arr = np.zeros(ct8)
wk9arr = np.zeros(ct9)
wk10arr = np.zeros(ct10)
wk11arr = np.zeros(ct11)
wk12arr = np.zeros(ct12)
wk13arr = np.zeros(ct13)
wk14arr = np.zeros(ct14)
wk15arr = np.zeros(ct15)
wk16arr = np.zeros(ct16)

#print(wk1arr)

ct1_a = 0
ct2_a = 0
ct3_a = 0
ct4_a = 0
ct5_a = 0
ct6_a = 0
ct7_a = 0
ct8_a = 0
ct9_a = 0
ct10_a = 0
ct11_a = 0
ct12_a = 0
ct13_a = 0
ct14_a = 0
ct15_a = 0
ct16_a = 0

for i in range(rows-1):
        if flow_data[i,1] == 8 and flow_data[i,2] >= 24 and flow_data[i,2] <= 30:
                wk1arr[ct1_a] = flow_data[i,3]
                ct1_a = ct1_a+1
        elif (flow_data[i,1] == 8 and flow_data[i,2] == 31) or (flow_data[i,1] == 9 and flow_data[i,2] >= 1 and flow_data[i,2] <= 6):
                wk2arr[ct2_a] = flow_data[i,3]
                ct2_a = ct2_a+1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 7 and flow_data[i,2] <= 13:
                wk3arr[ct3_a] = flow_data[i,3]
                ct3_a = ct3_a+1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 14 and flow_data[i,2] <= 20:
                wk4arr[ct4_a] = flow_data[i,3]
                ct4_a = ct4_a+1
        elif flow_data[i,1] == 9 and flow_data[i,2] >= 21 and flow_data[i,2] <= 27:
                wk5arr[ct5_a] = flow_data[i,3]
                ct5_a = ct5_a+1
        elif (flow_data[i,1] == 9 and flow_data[i,2] >= 28 and flow_data[i,2] <= 30) or (flow_data[i,1] == 10 and flow_data[i,2] >= 1 and flow_data[i,2] <= 4):
                wk6arr[ct6_a] = flow_data[i,3]
                ct6_a = ct6_a+1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 5 and flow_data[i,2] <= 11:
                wk7arr[ct7_a] = flow_data[i,3]
                ct7_a = ct7_a+1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 12 and flow_data[i,2] <= 18:
                wk8arr[ct8_a] = flow_data[i,3]
                ct8_a = ct8_a+1
        elif flow_data[i,1] == 10 and flow_data[i,2] >= 19 and flow_data[i,2] <= 25:
                wk9arr[ct9_a] = flow_data[i,3]
                ct9_a = ct9_a+1
        elif (flow_data[i,1] == 10 and flow_data[i,2] >= 26 and flow_data[i,2] <= 31) or (flow_data[i,1] == 11 and flow_data[i,2] == 1):
                wk10arr[ct10_a] = flow_data[i,3]
                ct10_a = ct10_a+1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 2 and flow_data[i,2] <= 8:
                wk11arr[ct11_a] = flow_data[i,3]
                ct11_a = ct11_a+1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 9 and flow_data[i,2] <= 15:
                wk12arr[ct12_a] = flow_data[i,3]
                ct12_a = ct12_a+1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 16 and flow_data[i,2] <= 22:
                wk13arr[ct13_a] = flow_data[i,3]
                ct13_a = ct13_a+1
        elif flow_data[i,1] == 11 and flow_data[i,2] >= 23 and flow_data[i,2] <= 29:
                wk14arr[ct14_a] = flow_data[i,3]
                ct14_a = ct14_a+1
        elif (flow_data[i,1] == 11 and flow_data[i,2] == 30) or (flow_data[i,1] == 12 and flow_data[i,2] >= 1 and flow_data[i,2] <= 6):
                wk15arr[ct15_a] = flow_data[i,3]
                ct15_a = ct15_a+1
        elif flow_data[i,1] == 12 and flow_data[i,2] >= 7 and flow_data[i,2] <= 13:
                wk16arr[ct16_a] = flow_data[i,3]
                ct16_a = ct16_a+1

#print(wk1arr)

weeklist = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
weeklist[0] = np.mean(wk1arr)
weeklist[1] = np.mean(wk2arr)
weeklist[2] = np.mean(wk3arr)
weeklist[3] = np.mean(wk4arr)
weeklist[4] = np.mean(wk5arr)
weeklist[5] = np.mean(wk6arr)
weeklist[6] = np.mean(wk7arr)
weeklist[7] = np.mean(wk8arr)
weeklist[8] = np.mean(wk9arr)
weeklist[9] = np.mean(wk10arr)
weeklist[10] = np.mean(wk11arr)
weeklist[11] = np.mean(wk12arr)
weeklist[12] = np.mean(wk13arr)
weeklist[13] = np.mean(wk14arr)
weeklist[14] = np.mean(wk15arr)
weeklist[15] = np.mean(wk16arr)

print(weeklist)


# %%
