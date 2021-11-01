list_example = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'x', 'f']
duplicates = []

for item in list_example:
    count = list_example.count(item)
    if(count > 1):
        if(item not in duplicates):
            duplicates.append(item)

print(duplicates)
