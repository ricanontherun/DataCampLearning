import pandas

import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

if __name__ == '__main__':
    home_data = pandas.read_csv(
        '../datasets/california-housing-data/housing.csv',
        usecols=['latitude', 'longitude', 'median_house_value'])

    plot = sns.scatterplot(data=home_data, x='longitude', y='latitude', hue='median_house_value')
    plot.get_figure().savefig('california-housing.png')
