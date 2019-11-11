import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import torch 
import seaborn as sns 
import datetime

# ## read data
data_path = "../data/yellow_tripdata_2019-01.csv"
df_read = pd.read_csv(data_path, index_col='tpep_pickup_datetime', parse_dates=True)
df_small = df_read['2019-01-01 00:00:00': '2019-01-01 00:30:00']

df = df_read # small for test, read for real statistics

# Get the number for each hour in one day
df.count()

# # ## get the location
# location = [x for x in range(1, 266)]


# f, ax = plt.subplots(figsize=(10,10))
# plt.ion()
# last_time = pd.to_datetime('2019-01-01 00:00:00')
# interval = 1

# for iter in range(24):
#     start = last_time
#     end = start + pd.Timedelta(interval, unit='h')
#     last_time = end
#     new_df = pd.DataFrame(np.zeros((265, 265)), columns=location, index=location)
    
#     df_part = df[str(start):str(end)]
#     print(df_part)

#     from_locs = df_part['PULocationID']
#     to_locs = df_part['DOLocationID']

#     for row in range(df_part.shape[0]):
#         from_id = int(from_locs[row])
#         to_id = int(to_locs[row])
#         new_df.iloc[from_id - 1, to_id - 1] += 1

#     plt.clf()
#     ax = sns.heatmap(new_df, vmin=0, vmax=100)
#     ax.set_title(f'Taxi data from {str(start)} to {str(end)}')
#     plt.pause(0.1)

# plt.ioff()    
# plt.show()

# print('Test over'.center(50, '-'))
