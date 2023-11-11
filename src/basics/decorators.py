print("Hello decors")


# @classmethod
# @staticmethod

def hello():
    print("Hellokjk")


greet = hello
del hello
print(greet())


def hello_de():
    pass

# Higher Order function HOC


def hoc(func):
    func()


def greet2():
    def func():
        return 10

    return func


def m_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")

    return wrap_func





@m_decorator
def hello():
    print("Hello")


hello()


a = m_decorator(hello)
print(a())




# def my_arg_decorator(func):
#     def wrap_func(x):
#         print("********")
#         func(x)
#         print("********")

#     return wrap_func



# @my_arg_decorator
# def h1(greet):
#     print(greet)



# h1("121")


# def h2(greet):
#     print(greet)



# a = my_arg_decorator(h2)
# a("kjkgjh")



def my_arg_decorator(func):
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")

    return wrap_func


@my_arg_decorator
def h3(greet, another):
    print(greet, another)



h3("121", "helll")


def h4(greet,another, name="Hello"):
    # pass
    print(greet,another,name)



a = my_arg_decorator(h4)
a("kjkgjh","another param", name="x")