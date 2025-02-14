# Some dict compprehension for: https://app.dataquest.io/c/162/m/644/python-dictionaries-and-frequency-tables/6/looping-over-dictionaries?path=2&slug=data-scientist&version=2.5
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

content_ratings = {key : (value/total_number_of_apps) * 100 for key, value in content_ratings.items()}

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = 100 - percentage_17_plus
