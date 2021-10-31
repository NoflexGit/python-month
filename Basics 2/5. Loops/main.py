items = [1, 2, 3, 4, 5]
items_tuple = ('a', False, 10.2, 90)

for x in items:
    print(x)

for y in items_tuple:
    print(y)

store = {
    'id': 1,
    'name': 'Amazon',
    'employees': 1800,
    'is_online': True
}

for key in store.keys():
    print(key)

for key, value in store.items():
    print(key, value)

for number in range(0, 1000):
    print(number)
