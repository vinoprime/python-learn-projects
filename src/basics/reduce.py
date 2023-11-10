# reduce
from functools import reduce
print("Hello Reduce")


my_list = [1, 2, 3]


def accumalator(acc, item):
    print(acc, item)
    return acc + item


res = reduce(accumalator, my_list, 0)
print(res)
