def exponention_of2(list):
    new_list = []
    for item in list:
        new_list.append(pow(item, 2))

    return new_list


print(exponention_of2([2, 4, 6]))


characters = [
    {'name': 'John'},
    {'name': 'Billy'}
]


def prepare_greetings(chars):
    greetings = []

    for item in chars:
        greetings.append(f'{item["name"]} says hi!')

    return greetings


print(prepare_greetings(characters))
