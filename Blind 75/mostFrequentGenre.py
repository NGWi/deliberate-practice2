# Me having fun with Dataquest lesson: 
# https://app.dataquest.io/c/162/m/644/python-dictionaries-and-frequency-tables/5/proportions-and-percentages?path=2&slug=data-scientist&version=2.5
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = dict()
for app in apps_data[1:]:
    genre = app[11]
    if genre in genre_counting:
        genre_counting[genre] += 1              
    else:
        genre_counting[genre] = 1

print(genre_counting)
# Drumroll, please...
print([key for key, value in genre_counting.items() if value == max([value for key, value in genre_counting.items()])])
# XD