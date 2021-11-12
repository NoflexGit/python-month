some_list = [2, 3, 4, 5, 6, 8, 10]


def check_odd(item):
    return item % 2 == 0


print(list(filter(check_odd, some_list)))


users = [
    {
        'name': 'John',
        'gender': 'male'
    },
    {
        'name': 'Nick',
        'gender': 'male'
    },
    {
        'name': 'Kate',
        'gender': 'female'
    }
]


def only_girls(item):
    return item['gender'] == 'female'


print(list(filter(only_girls, users)))
