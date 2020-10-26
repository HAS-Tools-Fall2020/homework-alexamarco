# Starter code for week 6 illustrating how to build an AR model
# and plot it

# %%
# Import the modules we will use
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def twoWeekForecasts(test_dataframe, model):
    """Compute the one and two week forecasts using model.
    ---------------------------------
    This function uses the last two results from the test
    data and extrapolates on them.  The most recent test
    result becomes the one week forecast.  The two week
    forecast is calculated by multiplying the most resent
    test result for the 1 day and 2 day coefficients and
    the second most recent result for the 5 day coefficients.
    ---------------------------------
    Parameters:
    test_dataframe - pandas dataframe
        Contains flow data from 1989 to now.
    model - sklearn regression model
        Provides coefficients for 1, 2, and 5 day flows.
    ----------------------------------
    Outputs:
    wk1_forecast - float
        One week forecast of streamflow.
    wk2_forecast - float
        Two week forecast of streamflow
    """
    series = test_dataframe['flow']
    series = series[:-2]
    coefficients = model.coef_
    wk1_forecast = series[2]
    wk2_forecast = coefficients[0] * series[0] + \
        coefficients[1] * series[0] + \
        coefficients[2] * series[1]
    return wk1_forecast, wk2_forecast


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath,
                     sep='\t',
                     skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Building an autoregressive model
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# with lagged timeseries
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)  # 1 day shift
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)  # 2 day shift
flow_weekly['flow_tm5'] = flow_weekly['flow'].shift(5)  # 5 day shift

# Step 2 - pick portions of time series for training & testing
# skip first 5 days b/c tm3 has a 5 day shift
# LC - you could think about defining these numbers as variables
train = flow_weekly[5:500][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm5']]
test = flow_weekly[500:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm5']]

# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
x = train[['flow_tm1', 'flow_tm2', 'flow_tm5']]
y = train['flow'].values
model.fit(x, y)

# Look at the results
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('slope:', np.round(model.coef_, 2))

# calculate regression manually and without intercept
# note! removing the intercept significantly improved the model
q_pred = model.coef_[0] * train['flow_tm1'] + model.coef_[1] \
        * train['flow_tm2'] + model.coef_[2] * train['flow_tm5']
q_pred_test = model.coef_[0] * test['flow_tm1'] + model.coef_[1] \
        * test['flow_tm2'] + model.coef_[2] * test['flow_tm5']

# Run function designed at top of script
# Gets 2 week forecast using AR model
forecasts = twoWeekForecasts(test, model)

print('week 1 regression forecast = ', forecasts[0])
print('week 2 regression forecast = ', forecasts[1])

print('week 1 forecast for submission = 70')
print('week 2 forecast for submission = 72')

# %%
# Plot comparison of training data, test results, and obs data
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full', color='C0')
ax.plot(q_pred_test, label='test', color='C4')
ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow VS. Model Prediction",
       xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(10, 6)
fig.savefig("Observed_Flow.png")

# %%
# Prepare 16 week forecasts

# get data from beginning of semester
filename1 = 'streamflow_week1.txt'
filepath1 = os.path.join('../../data', filename1)

# Read in fresh streamflow dataframe w/ week 1 data
data = pd.read_table(filepath1, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'])

# Expand the dates to year month day and set them as integers
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)  # year integer
data['month'] = data['month'].astype(int)  # month integer
data['day'] = data['day'].astype(int)  # day integer

# 65e9ee97251c4df881c319b8d639981c
# get averages for forecasting based on dates for each
# forecasting week of the semester

# LC - This is something you could put into a loop.
# you would just have to define the the months and days
# as lists outside your loop

# Week 1: 8/24-8/30
wk1mean = data[(data.month == 8) & (data.day >= 24) &
               (data.day <= 30)].flow.mean()

# Week 2: 8/31-9/6
wk2mean = data[((data.month == 8) & (data.day == 31)) |
               ((data.month == 9) &
               (data.day >= 1) & (data.day <= 6))].flow.mean()

# Week 3: 9/7-9/13
wk3mean = data[(data.month == 9) &
               (data.day >= 7) & (data.day <= 13)].flow.mean()

# Week 4: 9/14-9/20
wk4mean = data[(data.month == 9) &
               (data.day >= 14) & (data.day <= 20)].flow.mean()

# Week 5: 9/21-9/27
wk5mean = data[(data.month == 9) &
               (data.day >= 21) & (data.day <= 27)].flow.mean()

# Week 6: 9/28-10/4
wk6mean = data[((data.month == 9) &
               (data.day >= 28) & (data.day <= 30)) |
               ((data.month == 10) &
               (data.month >= 1) & (data.month <= 4))].flow.mean()

# Week 7: 10/5-10/11
wk7mean = data[(data.month == 10) &
               (data.day >= 5) & (data.day <= 11)].flow.mean()

# Week 8: 10/12-10/18
wk8mean = data[(data.month == 10) &
               (data.day >= 12) & (data.day <= 18)].flow.mean()

# Week 9: 10/19-10/25
wk9mean = data[(data.month == 10) &
               (data.day >= 19) & (data.day <= 25)].flow.mean()

# Week 10: 10/26-11/1
wk10mean = data[((data.month == 10) &
                (data.day >= 26) & (data.day <= 31)) |
                ((data.month == 11) & (data.day == 1))].flow.mean()

# Week 11: 11/2-11/8
wk11mean = data[(data.month == 11) &
                (data.day >= 2) & (data.day <= 8)].flow.mean()

# Week 12: 11/9-11/15
wk12mean = data[(data.month == 11) &
                (data.day >= 9) & (data.day <= 15)].flow.mean()

# Week 13: 11/16-11/22
wk13mean = data[(data.month == 11) &
                (data.day >= 16) & (data.day <= 22)].flow.mean()

# Week 14: 11/23-11/29
wk14mean = data[(data.month == 11) &
                (data.day >= 23) & (data.day <= 29)].flow.mean()

# Week 15: 11/30-12/6
wk15mean = data[((data.month == 11) & (data.day == 30)) |
                ((data.month == 12) &
                (data.day >= 1) & (data.day <= 6))].flow.mean()

# Week 16: 12/7-12/13
wk16mean = data[(data.month == 12) &
                (data.day >= 7) & (data.day <= 13)].flow.mean()


# Put each week's forecast into a comma separated list
forecasts = [wk1mean, wk2mean, wk3mean, wk4mean,
             wk5mean, wk6mean, wk7mean, wk8mean,
             wk9mean, wk10mean, wk11mean, wk12mean,
             wk13mean, wk14mean, wk15mean, wk16mean]
print('Weekly Forecasts:', forecasts)

# %%
