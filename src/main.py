# name = input("Enter:")
# print("Hello"+name)

# Data Types
int # 12
float # 65.25
bool # True/false
str # "Hello String"
list # []
tuple
set # ()
dict # []
None # absence of value/ means nothing


#  Classes -> Custom types
# Specialized Data Types -> Modules


# int
print(1+2)
print(1-2)
print(1 * 2)
print(1 / 2)
print(2 ** 2)
print(2 // 4)
print(6 % 4)
print(type(3))
# float
print(1.5)
print(type(1.5))

# bool
print(True)
# str
print("Hello str")



# Math
print(round(1.26))
print(abs(-12))

# Operator Precedence
print(20+3*4) # 20+(3*4)

# ()
# **
# * /
# + -

# Complex
print(complex(1,2.0)) # (1+2j)


print(bin(5)) #0b101
print(oct(5))
print(hex(5))

print(int("0b101", 2))



a,b,c = 11,2,3

# print(a)

aa = 10
bb = 2
bb +=2
bb -=2
bb *=2



# str
print(type("kjdfhgfhd"))
# log string
l_str = """
Hello long str
"""

print(l_str)


# Escape sequences

w = "It's sunny"
w1 = "It \'s \"knid"
w2 = "\tIt \'s \"knid"
print(w1)
print(w2)

# Formated string
name = "VVVV"
print(f"{name}")

# Expressions and statements

if a ==1 :
    print("10")
elif a==5:
    print("100")
else:
    print("else")



#  Password checker
# name = input("Enter name: ")
# passwd = input("Enter pass: ")

# print(f"your pass is {len(passwd)}")

# List
li = [1,2,3,"fgfg"]
li[0] = "dfdf"
print(li)

# List Slicing
a_cart = [
    "note",
    "sun",
    "toy",
    "boy",
]

print(a_cart[1:3]) # it creates new list

# Matrix
# the way to discribe 2d

# 2D Array example
matrix = [
    [1,2,3],
    [4,5,6],
    [9,6,3]
]

print(matrix[2][1])

basket = [1,2,3,4,5]
print(len(basket))

# Adding
n_lsit = basket.insert(2,100)
n_lsit = basket.append(6) # it dosen't produce any value , just it change the value in list
n_lsit = basket.extend([5,6])
print(basket)
print(n_lsit)

# Removing
basket.pop()
basket.pop(2) # give value to remove
basket.remove(2) # give index to remove
basket.clear()


print(basket)


# List unpacking
bas = [1,2,3,4,5]
a,b,c, *other,d = bas

print(a,b,c, other,d)


# Dictionary (unorderred key value pair)
print(dict)
# sytntax
d = { "a":1, "b":2, "c":[1,2,3], "d":"Hello", 123:"xyz", True: "he"} # {key, value}
print(d)
print(d['b'])
print(d['c'])
print(d['c'][0])
print(d[123])
print(d[True])

# Safe way to get value from dict
print(d.get("x"))
print(d.get("x", 55))


val = "vvv"
user = dict(key=val)
print(user)


# Tuple like list but it is immutable (Readonly list)
tup = (1,2,3,4,5)
print(tup)
print(tup[0])