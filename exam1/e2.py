import json
from functools import reduce 
import re

with open("people.json") as f:
   data = json.load(f)

for it in data:
   for ids in it.get('friends'):
       print(ids.get('eyeColor'))
   
print(*friend_data)
print(friend_data['eyeColor'])

len_friends = list(filter(lambda y:  y['eyeColor'] == 'blue', friend_data))
print(len_friends)
min_count = min(len_friends)

out = map(lambda it: it['name'], list(filter(lambda it: len(it['friends']) == min_count, data)))
print(*out)
