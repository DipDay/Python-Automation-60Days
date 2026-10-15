import pandas as pd

# data = [101.2, 100, 209, 208.53]
# series = pd.Series(data, index=['a', 'b', 'c', 'd'])
# # print(series)
# # print(series.loc['c'])
# # print(series.iloc[0])
# print(series[series > 200])

calories = {'day 01': 1600, 'day 02': 2200, 'day 03': 1150}
series = pd.Series(calories)
series.loc['day 01'] += 700 
# print(series)
print(series.loc['day 01'])


