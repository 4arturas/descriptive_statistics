import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hw = pd.read_csv('D:\PycharmProjects\DescriptiveStatistics\datasets\Person_Gender_Height_Weight_Index.csv')
# print(hw.head())
# print(hw.columns)

# print( hw.columns.values )
colWeight = "Weight"
mean = hw[colWeight].mean()

median = hw[colWeight].median()

listOfSeries = [pd.Series(['Male', 205, 460,1], index=hw.columns.values ),
                pd.Series(['Female', 202, 390,1], index=hw.columns.values ),
                pd.Series(['Female', 199, 410,1], index=hw.columns.values ),
                pd.Series(['Male', 202, 390,1], index=hw.columns.values ),
                pd.Series(['Female', 199, 410,1], index=hw.columns.values ),
                pd.Series(['Male', 200, 490,1], index=hw.columns.values )]

hw = hw.append( listOfSeries )
# print( hw.tail() )

mean_new = hw[colWeight].mean()

print('Mean=', mean)
print("MeanNew={0}".format( mean_new ) )
print()

median_new = hw[colWeight].median()
print("Median={0}".format(median))
print("MedianNew={0}".format( median_new ))

plt.subplot(211)
hw[colWeight].hist(bins=100)
plt.axvline( mean_new, color='r', label="mean")
plt.axvline( median_new, color='g', label="median")
plt.legend()


colHeight = "Height"
height_counts = {}
for height in hw[colHeight] :
    if height not in height_counts :
        height_counts[height] = 1
    else :
        height_counts[height] += 1

count = 0
size = 0
for s, c in height_counts.items():
    if count < c:
        count = c
        size = s
print("Size: {0}\nFrequency: {1}".format(size, count))

plt.subplot(212)
x_range = range(len(height_counts))
plt.bar( x_range, list(height_counts.values()), align="center")
plt.xticks( x_range, list(height_counts.keys()) )
plt.xlabel("Height")
plt.ylabel("Count")

plt.show()