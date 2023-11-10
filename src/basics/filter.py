print("Hello filter")



def only_odd(num):
    return num % 2 !=0


ers = filter(only_odd, [1,2,3])
print(list(ers))