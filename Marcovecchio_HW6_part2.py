# Example solution for HW 4

# %%
# Import the modules we will use
import os
import pandas as pd

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
                     )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


# %%
# get weekly averages for forecasting
# takes the average of streamflow for each course week from total dataset
# identifies indices that fall within a certain day & month range
# then takes the mean of those indices

# Wk 1: Aug 8 to Aug 30
wk1mean = data[(data.month == 8)
               & (data.day >= 24) & (data.day <= 30)].flow.mean()

# Wk 2: Aug 31 to Sep 6
wk2mean = data[((data.month == 8) & (data.day == 31))
               | ((data.month == 9)
               & (data.day >= 1) & (data.day <= 6))].flow.mean()

# Wk 3: Sep 7 to Sep 13
wk3mean = data[(data.month == 9)
               & (data.day >= 7) & (data.day <= 13)].flow.mean()

# Wk 4: Sep 14 to Sep 20
wk4mean = data[(data.month == 9)
               & (data.day >= 14) & (data.day <= 20)].flow.mean()

# Wk 5: Sep 21 to Sep 27
wk5mean = data[(data.month == 9)
               & (data.day >= 21) & (data.day <= 27)].flow.mean()

# Wk 6: Sep 28 to Oct 4
wk6mean = data[((data.month == 9) & (data.day >= 28) & (data.day <= 30))
               | ((data.month == 10)
               & (data.month >= 1) & (data.month <= 4))].flow.mean()

# Wk 7: Oct 5 to Oct 11
wk7mean = data[(data.month == 10)
               & (data.day >= 5) & (data.day <= 11)].flow.mean()

# Wk 8: Oct 12 to Oct 18
wk8mean = data[(data.month == 10)
               & (data.day >= 12) & (data.day <= 18)].flow.mean()

# Wk 9: Oct 19 to Oct 25
wk9mean = data[(data.month == 10)
               & (data.day >= 19) & (data.day <= 25)].flow.mean()

# Wk 10: Oct 26 to Nov 1
wk10mean = data[((data.month == 10) & (data.day >= 26) & (data.day <= 31))
                | ((data.month == 11) & (data.day == 1))].flow.mean()

# Wk 11: Nov 2 to Nov 8
wk11mean = data[(data.month == 11)
                & (data.day >= 2) & (data.day <= 8)].flow.mean()

# Wk 12: Nov 9 to Nov 15
wk12mean = data[(data.month == 11)
                & (data.day >= 9) & (data.day <= 15)].flow.mean()

# Wk 13: Nov 16 to Nov 22
wk13mean = data[(data.month == 11)
                & (data.day >= 16) & (data.day <= 22)].flow.mean()

# Wk 14: Nov 23 to Nov 29
wk14mean = data[(data.month == 11)
                & (data.day >= 23) & (data.day <= 29)].flow.mean()

# Wk 15: Nov 30 to Dec 6
wk15mean = data[((data.month == 11) & (data.day == 30))
                | ((data.month == 12)
                & (data.day >= 1) & (data.day <= 6))].flow.mean()

# Wk 16: Dec 7 to Dec 13
wk16mean = data[(data.month == 12)
                & (data.day >= 7) & (data.day <= 13)].flow.mean()

forecasts = [wk1mean, wk2mean, wk3mean, wk4mean,
             wk5mean, wk6mean, wk7mean, wk8mean,
             wk9mean, wk10mean, wk11mean, wk12mean,
             wk13mean, wk14mean, wk15mean, wk16mean]
print("16 Week Forecast: \n", forecasts)

# %%
