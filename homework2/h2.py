#Given file containing film name and author in each line. Find all films for the given author. Author name will be passed by keyboard.

def read_file(file_name):
    hash = {}
    with open(file_name) as file:
        for line in file:
            (key, value) = line.split()
            hash[key] = value
    return hash

def get_keys_by_value(hash, author):
    l = []
    items = hash.items()
    for it in items:
        if it[1] == author:
            l.append(it[0])
    return l

s = read_file("n.txt")
i = input()
print(get_keys_by_value(hash = s, author = i))
