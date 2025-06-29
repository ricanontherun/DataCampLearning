import pandas

import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

if __name__ == '__main__':
    # Read the dataset with Pandas
    home_data = pandas.read_csv(
        '../datasets/california-housing-data/housing.csv',
        usecols=['latitude', 'longitude', 'median_house_value'])

    # Split our data into train and testing data.
    # We will use 33% of the data for testing and the rest for training.
    X_train, X_test, y_train, y_test = train_test_split(home_data[['latitude', 'longitude']], home_data[['median_house_value']], test_size=0.33, random_state=0)

    # Normalize the data
    X_train_norm = preprocessing.normalize(X_train)
    X_test_norm = preprocessing.normalize(X_test)

    kmeans = KMeans(n_clusters=3, random_state=0, n_init='auto')
    estimator = kmeans.fit(X_train_norm)

    # plot = sns.scatterplot(data=X_train, x='longitude', y='latitude', hue=kmeans.labels_)
    # plot.get_figure().savefig('california-housing-kmeans.png')

    box_plot = sns.boxplot(x=kmeans.labels_, y=y_train['median_house_value'])
    box_plot.get_figure().savefig('california-housing-value-boxplot.png')

