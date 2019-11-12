import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import torch 
import seaborn as sns 
import datetime

# ## read data
data_path = "../data/yellow_tripdata_2019-01.csv"
print('Reading file...')
df_read = pd.read_csv(data_path, nrows=1000000, index_col='tpep_pickup_datetime', parse_dates=True)
df_small_1 = df_read['2019-01-01 00:00:00': '2019-01-02 00:00:00']
df_small_2 = df_read['2019-01-02 00:00:00': '2019-01-03 00:00:00']
df_small_3 = df_read['2019-01-03 00:00:00': '2019-01-04 00:00:00']

df = df_small_2 # small for test, read for real statistics

# Get the number for each hour in one day
# appear_time = pd.DataFrame(list(df.index), columns=['Time'])
# print(appear_time)
# sample = appear_time.resample('15T', on='Time', label='right').count()
# print(sample)

# fig = plt.subplots(figsize=(20, 8))
# plt.plot(sample.index.strftime('%Y-%m-%d %H:%M:%S'), list(sample.values))
# plt.xlabel('Time')
# plt.xticks(np.arange(0, len(sample.values), 12))
# plt.ylabel('Taxi usage')
# plt.title(f'Taxi usage of NYC in 2019-01-02')
# plt.savefig('figures/NYC-2019-01-02.png')
# plt.show()

# ## get the location
location = [x for x in range(1, 266)]

f, ax = plt.subplots(figsize=(10,10))
plt.ion()
last_time = pd.to_datetime('2019-01-02 00:00:00')
interval = 1

for iter in range(24):
    start = last_time
    end = start + pd.Timedelta(interval, unit='h')
    last_time = end
    new_df = pd.DataFrame(np.zeros((265, 265)), columns=location, index=location)
    
    df_part = df[str(start):str(end)]
    print(df_part.info())

    from_locs = df_part['PULocationID']
    to_locs = df_part['DOLocationID']

    for row in range(df_part.shape[0]):
        from_id = int(from_locs[row])
        to_id = int(to_locs[row])
        new_df.iloc[from_id - 1, to_id - 1] += 1

    plt.clf()
    ax = sns.heatmap(new_df, vmin=0, vmax=100)
    ax.set_title(f'Taxi data from {str(start)} to {str(end)}')
    plt.pause(0.1)

plt.ioff()    
plt.show()

print('Test over'.center(50, '-'))
