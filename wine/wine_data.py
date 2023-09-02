import pandas as pd
reviews = pd.read_csv('../data/winemag-data-130k-v2.csv', index_col=0)
#print(reviews)
data_count = reviews.groupby('country').points.mean().round(1)
#print(data_count)
data_sort = reviews.country.value_counts()
#print(data_sort)
data = pd.merge(data_sort, data_count, on='country')
#print(data)
data.to_csv('reviews-per-country.csv')
