# map
print("Hello map")


def mul_by2(item):
    return item*2

# map's params is immutable
res = map(mul_by2, [1, 2, 3])
data= list(res)
print(data)
