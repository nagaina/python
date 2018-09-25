#Given a file containing a number in each line. Read the file, remove duplicates and sort the file.

def read_file_and_remove_duplicates(file_name):
    with open(file_name) as file:
        s = set(file.read().split())
    return s

s = read_file_and_remove_duplicates("numbers.txt")
print(sorted(s, key = int))
