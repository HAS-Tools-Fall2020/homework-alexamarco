Alexa Marcovecchio
September 21, 2020
Assignment 4

Forecast Summary:
The code for this forecast is in my homework folder and includes the scripts Marcovecchio_HW4_part1.py and Marcovecchio_HW4_part2.py.  Marcovecchio_HW3_part1.py generates the 16 week forecast using the week 1 daily streamflow data from USGS as well as the quantile and histogram analysis.  The method used was essentially the same as last week.  However, arrays added a layer of difficulty because you need to know the dimensions of an array to make the code work properly.  I used a for loop to find the number of entries in each week and then applied the same algorithm I used last week with the addition of an extra counter to index each array entry. I then made histograms and quantile analyses for both week 5 and 6 because those are the 1 week and 2 week predictions for this week.  The histogram showed that the smallest streamflow was the most common, and I also selected values below the 1st quantile because I know that we're in a drought. Marcovecchio_HW3_part2.py generates the answers to questions 3 through 5 using the same methodology as last week, but modified for arrays.

Assignment Questions
1. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.
    **see forecast summary above
2. Describe the variable flow_data:
    Flow data has 46526 entries and dimensions(11564,4).  Column 0 = year, column 1 = month, column 2 = day, and column 3 = streamflow value.
3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
    Daily flow was greater than my predictions in the month of September (work shown in Marcovecchio_HW4_part2.py) 276 times at a percentage rate of 25.4%.
4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
    In or before 2000: 152 times at 36.2%
    In or after 2010: 65 times at 18.6%
5. How does the daily flow generally change from the first half of September to the second?
    Daily flow seems to fluctuate throughout the month of September, and again does not show a consistent increasing or decreasing monthly trend over the years.  According to my weekly predictions, streamflow is increasing in the first half of September, drops in the middle of the month, and then increases again for the second half of September.