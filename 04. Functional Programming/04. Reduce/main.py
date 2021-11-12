from functools import reduce


def reducer_func(acc, el):
    return acc + el


print(reduce(reducer_func, [1, 2, 3, 4, 5]))
print(reduce(reducer_func, [20, 299, 33, 1, 0]))
print(reduce(reducer_func, ['I ', 'eat ',
      'fresh ', 'fruits ', 'every ', 'day!']))
