def exponention_of2(item):
    return pow(item, 2)

exponented = map(exponention_of2, [2, 4, 6])

print(list(exponented))
