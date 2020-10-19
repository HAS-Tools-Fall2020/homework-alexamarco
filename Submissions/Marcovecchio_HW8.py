# Starter code for week 6 illustrating how to build an AR model
# and plot it

# %%
# Import the modules we will use
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
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
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(5)  # 5 day shift

# Step 2 - pick portions of time series for training & testing
# skip first 5 days b/c tm3 has a 5 day shift
train = flow_weekly[5:500][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]
test = flow_weekly[500:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]

# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
x = train[['flow_tm1', 'flow_tm2', 'flow_tm3']]
y = train['flow'].values
model.fit(x, y)

# Look at the results
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# calculate regression without intercept
# note! removing the intercept significantly improved the model
q_pred = model.coef_[0] * train['flow_tm1'] + model.coef_[1] \
        * train['flow_tm2'] + model.coef_[2] * train['flow_tm3']
q_pred_test = model.coef_[0] * test['flow_tm1'] + model.coef_[1] \
        * test['flow_tm2'] + model.coef_[2] * test['flow_tm3']


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


forecasts = twoWeekForecasts(test, model)

print('week 1 regression forecast = ', forecasts[0])
print('week 2 regression forecast = ', forecasts[1])

print('week 1 forecast for submission = 58')
print('week 2 forecast for submission = 60')

# %%
