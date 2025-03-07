# Solution without sorting (see my comment regarding that below) for
# https://app.dataquest.io/c/162/m/644/python-dictionaries-and-frequency-tables/9/filtering-for-the-intervals?path=2&slug=data-scientist&version=2.5

from math import log10
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_ratings = [int(app[5]) for app in apps_data[1:]]
min_ratings = min(n_ratings)
max_ratings = max(n_ratings)

frequencyBins = {}
bins = round(log10(max_ratings - min_ratings))
interval_mult = round(max_ratings ** (1/(bins - 1)))
start = 0
ceiling = 1
""" I opted to single out all the apps with no ratings 
despite going over the recommendation of 5 bins or less."""
while start < max_ratings: 
    """ Will do loops == bins == log n, O(n * log n).
    So it would be more efficient to sort the ratings first,
    a one time operation, reducing it to one pass forO(n)"""
    if ceiling > max_ratings:
        ceiling = max_ratings + 1
    interval = f'{start}-{ceiling - 1}' if start != 0 else '0'
    frequencyBins[interval] = 0
    for rating in n_ratings:
        if start <= rating < ceiling:
            frequencyBins[interval] += 1
    start = ceiling
    ceiling = ceiling * interval_mult

print(frequencyBins)