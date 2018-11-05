import json
from functools import reduce 
import re

with open("people.json") as f:
    data = json.load(f)


friends = map(lambda it: list(map(lambda x: x.get('eyeColor'), it.get('friends'))), data)
blue_count = map(lambda x : len(list(filter(lambda i : i == 'blue', x))), friends)
max_blue = max(blue_count)

out = map(lambda it: it['name'], list(filter(lambda x : len(list(filter(lambda i : i == 'blue', x))) < max_blue, data)))

print(*out)
