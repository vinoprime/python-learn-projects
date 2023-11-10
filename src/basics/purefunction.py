print("Hello Pure Function")

# input is [1,2,3] => function -> [2,4,6] => every time run this it gives the same output this input
# does not affect outside of the function


# Pure function example
def mul_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)

    return new_list


# not Pure function example
def mul_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    # here accessing outside
    return print(new_list)


# not Pure function example
new_list = []
def mul_by2(li):
    for item in li:
        new_list.append(item*2)

    return new_list


print(mul_by2([1, 2, 3]))
