Alexa Marcovecchio
September 14, 2020
Assignment 3

Forecast Summary:
The code for this forecast is in my homework folder and includes the scripts Marcovecchio_HW3_part1.py and Marcovecchio_HW3_part2.py.  ts Marcovecchio_HW3_part1.py generates the 16 week forecast using the week 1 daily streamflow data from USGS.  I use a for loop to go through each index in the flow array provided.  I then use if and elif statements with combined conditionals to make a list of all data points for each forecasting week since 1989 by specifying the day and month of each date, but not the year.  I then average each week's data and append that average to the list of weekly streamflow predictions. Marcovecchio_HW3_part2.py generates my forecasting estimates for next week and the following week using the same methods as the first script, but with more recent data included (from 1989 to this past Saturday).

Assignment Questions
1. Describe the variables flow, year, month, and day. What type of objects are they, what are they composed of, and how long are they?
    flow = list object composed of flow values for each date with length 11564
    year = list object of same length as flow containing the year value for each entry in flow
    month = list object of same length as flow containing the month value for each entry in flow
    day = list object of same length as flow containing the day value for each entry in flow
2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
    Daily flow was greater than my predictions in the month of September (work shown in Marcovecchio_HW3_part2.py) 235 times at a percentage rate of 24.9%.
3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
    In or before 2000: 132 times at 36.6%
    In or after 2010: 52 times at 16.6%
4. How does the daily flow generally change from the first half of September to the second?
    Daily flow seems to fluctuate throughout the month of September.  According to my weekly predictions, streamflow is increasing in the first half of September, drops in the middle of the month, and then increases again for the second half of September.