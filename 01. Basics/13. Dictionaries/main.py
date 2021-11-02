dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

list_of_dictionaries = [{
    'a': 1,
}, {
    'b': 2,
}]

print(dictionary['a'])
print(list_of_dictionaries[1]['b'])

print(dictionary.get('f'))  # None
print(dictionary.get('x', 'Set x'))

list_of_dictionaries[1].clear()
print(list_of_dictionaries)
