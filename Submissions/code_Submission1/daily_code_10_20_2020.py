# %%
import pandas as pd
import os
import numpy as np

# 1) Load in your streamflow timeseries from your data folder like this:
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code']),
                     parse_dates=['datetime'], index_col='datetime'
                     )
# Return the streamflow January 3-5 as many ways as you can
# *1989
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)  # year integer
data['month'] = data['month'].astype(int)  # month integer
data['day'] = data['day'].astype(int)  # day integer

print(data)

wk1mean = data[(data.month == 1) & (data.day >= 3) &
               (data.day <= 5)].flow

# %%
