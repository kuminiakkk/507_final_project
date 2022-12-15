import json

f = open('tree_Voting.json')

data_voting = json.load(f)

f1 = open('tree_Popularity.json')

data_popularity = json.load(f1)

f2 = open('tree_Release_date.json')

data_release_date = json.load(f2)