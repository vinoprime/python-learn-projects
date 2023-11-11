print("Hello Generators")

range(100)  # is a generators
# list(100) # is a itterable


z = list(range(10))
print(z)


def geneartor_func(num):
    for i in range(num):
        yield i*2


for item in geneartor_func(10):
    print(item)

g = geneartor_func(10)
print(g)
next(g)
print(next(g))


def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


my_for_loop([1, 2, 3])


class MyGen():

    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 10)


for i in gen:
    print(i)
