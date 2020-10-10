# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
#note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

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
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(5)

# Step 2 - pick what portion of the time series you want to use as training data
# skip first 5 days b/c of tm3 has shift 5
train = flow_weekly[5:][['flow', 'flow_tm1', 'flow_tm2','flow_tm3']]
test = flow_weekly[5:][['flow', 'flow_tm1', 'flow_tm2','flow_tm3']]

# Step 3: Fit a linear regression model using sklearn 
model = LinearRegression()
x=train[['flow_tm1','flow_tm2','flow_tm3']]
y=train['flow'].values
model.fit(x,y)

#Look at the results
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

#alternatievely you can calculate this yourself like this: 
q_pred_train = model.predict(train[['flow_tm1', 'flow_tm2','flow_tm3']])
q_pred = model.intercept_ + model.coef_[0] * train['flow_tm1'] + model.coef_[1] * train['flow_tm2'] + model.coef_[2] * train['flow_tm3'] 



# %% 
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed flow values
# Note that date is the index for the dataframe so it will 
# automatically treat this as our x axis unless we tell it otherwise
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full', color = 'C0')
ax.plot(q_pred, label = 'prediction', color = 'C3')
#ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow VS. Model Prediction", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(10,6)
fig.savefig("Observed_Flow.png")


# 3. Line  plot comparison of predicted and observed flows
#fig, ax = plt.subplots()
#ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
#ax.plot(train.index, q_pred_train, color='green', linestyle='--', 
#        label='simulated')
#ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
#        yscale='log')
#ax.legend()

# 4. Scatter plot of t vs t-1 flow with log log axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='shift1')
ax.scatter(train['flow_tm2'], train['flow'], marker = 'p',
              color = 'yellowgreen', label = 'shift2')
ax.scatter(train['flow_tm3'], train['flow'], marker = 'p',
              color = 'dodgerblue', label = 'shift5')
ax.set(xlabel='flow t minus shift', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow']), np.sort(q_pred_train), label='AR model', color = 'firebrick')
ax.legend()

# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

plt.show()


# %%
