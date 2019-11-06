# Dataset Description

> In this document, multiple frequently used datasets in traffic flow prediction will be introduced. They vary in their size, content, publicity and accessibility. A fraction of them are accompanied with visualizations. Besides, frequent measurements used will also be displayed along with the easy Python code.

## METR-LA

This dataset comes from the communications of the ACM, 2014 Big Data and Its Technical Challenges. It’s the speed captured from the loop detectors installed in the highway of Los Angeles County. There are **207** sensors and the data are collected for 4 months from May 1st 2012 to Jun 30th 2012. The data was processed into **5 min windows**. Thus for each day, there are **288 samples/day** . The file is stored in `.h5` file and should be opened with python module `hd5y`. The data can be read with the following code

```Python
# ## Read the metr_la data
data_name = 'metr-la'
data_path = 'data/' + data_name + '.h5'
df = pd.read_hdf(data_path)
print(df.shape)
print(df)
```

In this way, the read dataframe is with shape **(34727, 207)**. The column is the sensor id while the index is the timestamp of the data caputred. The visualization of the data is as follows:

![Figure 1](./figures/metr_la_773869_2012-03-01.png)

## PEMS-BAY

PEMS-Bay is collected b California Transportation Agencies Performance Measurement Systems. There are **325** sensors for **6 months** data ranging from 1st 2017 to May 31tst 2017. The data is still windowed in **5 min** window width. In can be read in the following code

```python
# ## Read the pems_bay data
data_name = 'pems-bay'
data_path = 'data/' + data_name + '.h5'
df = pd.read_hdf(data_path)
print(df.shape)
print(df)
```

In this way, the read dataframe is with shape **(52116, 325)**. The column is the sensor id while the index is the timestamp of the data caputred. The visualization of the data is as follows:

![Figure 2](figures/pems-bay_400001_2017-01-01.png)

## NYC Bike
