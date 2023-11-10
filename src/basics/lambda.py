from functools import reduce
print("Hello Lambda")
# One time annoymous functions

my_list = [1, 2, 3]
# Syntax
# lambda param1,param2 : param1 + param2 
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 0))


m_list = [5,4,3]

new_lst = list(map(lambda num: num**2, m_list))
print(new_lst)

# List Sort
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort()
a.sort(key= lambda x: x[1])
print(a)

