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
# get averages for forecasting

wk1mean = data[(data.month == 8) & (data.day >= 24) & (data.day <= 30)].flow.mean()

wk2mean = data[((data.month == 8) & (data.day == 31)) | ((data.month==9) & (data.day >= 1) & (data.day <= 6))].flow.mean()

wk3mean = data[(data.month == 9) & (data.day >= 7) & (data.day <= 13)].flow.mean()

wk4mean = data[(data.month == 9) & (data.day >= 14) & (data.day <= 20)].flow.mean()

wk5mean = data[(data.month == 9) & (data.day >= 21) & (data.day <= 27)].flow.mean()

wk6mean = data[((data.month == 9) & (data.day >= 28) & (data.day <= 30)) | ((data.month == 10) & (data.month >= 1) & (data.month <= 4))].flow.mean()

wk7mean = data[(data.month == 10) & (data.day >= 5) & (data.day <= 11)].flow.mean()

wk8mean = data[(data.month == 10) & (data.day >= 12) & (data.day <= 18)].flow.mean()

wk9mean = data[(data.month == 10) & (data.day >= 19) & (data.day <= 25)].flow.mean()

wk10mean = data[((data.month == 10) & (data.day >= 26) & (data.day <= 31)) | ((data.month ==11) & (data.day == 1))].flow.mean()

wk11mean = data[(data.month == 11) & (data.day >= 2) & (data.day <= 8)].flow.mean()

wk12mean = data[(data.month == 11) & (data.day >= 9) & (data.day <= 15)].flow.mean()

wk13mean = data[(data.month == 11) & (data.day >= 16) & (data.day <= 22)].flow.mean()

wk14mean = data[(data.month == 11) & (data.day >= 23) & (data.day <= 29)].flow.mean()

wk15mean = data[((data.month == 11) & (data.day == 30)) | ((data.month == 12) & (data.day >= 1) & (data.day <= 6))].flow.mean()

wk16mean = data[(data.month == 12) & (data.day >= 7) & (data.day <= 13)].flow.mean()

forecasts = [wk1mean,wk2mean,wk3mean,wk4mean,wk5mean,wk6mean,wk7mean,wk8mean,wk9mean,wk10mean,wk11mean,wk12mean,wk13mean,wk14mean,wk15mean,wk16mean]
print(forecasts)


# %%
