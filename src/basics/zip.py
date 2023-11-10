# zip
print("Hello Zip")

my_list = [1, 2, 3]
your_list = [10, 20, 30, 40]
their_list = (100, 200, 300)
our_list = {"key1": 123, "key2": 321}


res = zip(my_list, your_list)
print(list(res))  # output [(1, 10), (2, 20), (3, 30)]
res = zip(my_list, your_list, their_list)
print(list(res))  # output [(1, 10, 100), (2, 20, 200), (3, 30, 300)]
res = zip(my_list, your_list, our_list)
print(list(res))  # output [(1, 10, 'key1'), (2, 20, 'key2')]
