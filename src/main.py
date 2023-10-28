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
d = { "a":1, "b":2, "c":[1,2,3], "d":"Hello", 123:"xyz", True: "he", (1,2):"tuple"} # {key, value}
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
tup = (1,2,3,4,5,1)
a,b,c, *other = (1,2,3,4,5)
print(tup)
print(tup[0])
n_tup = tup[1:2]
print(n_tup)
print(a,b,c,other)
print(tup.count(1))
print(tup.index(5))

# Sets unordered collection of unique object 
my_set = {1,2,3,4,5,5}
print(my_set) # there is no duplicates allowed

# Remove duplicates
m_list = [1,2,1,2]
res = set(m_list)
print(res)
m_list = list(res)
print(m_list)


# Flow control
is_old = False
is_li = True

if is_old:
    print("Your are old")

print("che")

# Ternary
can = "msg" if is_old else "not"

print(can)

# Short Circuting
is_frd = True
is_u = False

print(is_frd or is_u)


# is vs
print(True is True) # True
print([] is []) # Flase because different mem


# Loops
for item in "Zoo":
    print(item)

for item in (1,2,3):
    print(item)

for it in ["a", "b", "c"]:
    print(it)

for it in {1,2,3,4,5}:
    print(it)

# Iterratable - list, dict, tuple, set. string
#  Iterate -> one by one check in each collection
for it in {"a":1,"b":[0,1,2]}.items():
    key, value = it
    print(it)

for key, value in {"a":1,"b":[0,1,2]}.items():
    print(key, value)

for it in {"a":1,"b":[0,1,2]}.values():
    print(it)
for it in {"a":1,"b":[0,1,2]}.keys():
    print(it)



# Range
print(range(100))
print(range(0,50))
print(list(range(100)))


for num in range(0,10):
    print(num)

for _ in range(0,10,2):
    print(_)

for _ in range(10,0,-1):
    print(_)



# Enumerate
for idx, char in enumerate("Hello"):
    print(idx,char)
for idx, char in enumerate([45,55]):
    print(idx,char)

# While
i=0
while i < 50:
    i += 1
    print(i)
    print("Brek")
    break
else: # else execute only without brek inside while
    print("Done")


for num in [1,2,3]:
    continue
    print(num)

for num in [1,2,3]:
    pass
    print(num)



# excercise
pic =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]


for row in pic:
    for px in row:
        if px == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")


# Functions

def fun_name():
    print("Hello")


fun_name()

#  Parameters
def disp(val, val2):
    print(f"Hello {val}")


# Args
disp("val", "ddffd")

# Default Params
def disp(val="defalut", val2=2):
    print(f"Hello {val}")


# keyword Args
disp(val2="Hello")

# Methods vs Functions
list() # function
print() # function



"hello".capitalize()  # capitalize()  is a Method



# args vs kwargs

def a_func(*args, **kwargs):
    print(*args)
    print(args)
    print(kwargs)
    return sum(args)


a_func(1,2,3,4, num1=5)

# Rule : params , *args, default params, **kwargs
# def fn(name, *args, age=10, **kwargs):


# Walurus operator  => :=

a = "Helloooooooooooo"
if len(a) > 10:
    print(f"too long {len(a)} elements")

a = "Helloooooooooooo"
if (n := len(a)) > 10:
    print(f"too long {n} elements")

# Scope
# Global scope
# function scope

if True:
    x=10

def b_func():
    total =100
    print(x)

# print(total) # not scoped
b_func()

# Scope rule

a=1
def confuse():
    # it has its own spcase with new a
    a=5
    return a

print(a)
print(confuse())
print(a)

# Strat with local?
# Parent local?
# Global?
# Built in Python


# Global keyword
b=10
def confuse():
    global b 
    b +=5
    return b


print(confuse())

# nonlocal