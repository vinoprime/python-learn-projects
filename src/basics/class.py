

class BigObject:

    # Class Object Attribute
    member = True

    def __init__(self, name, age=8):
        self.name = name  # Attributes
        self.age = age

    def printHello(self, name: str):
        print(f"Hello {name}")

    def printName(self):
        print(self.name)


obj = BigObject("Vinoth")
obj1 = BigObject("Rag")

obj.printName()
obj1.printName()
print(obj.member)
obj.member = False
print("From obj1 : ", obj1.member, obj1.age)
print("From obj : ", obj.member)


class StaticObject:

    def __init__(self):
        return

    # If you need props then use this
    @classmethod
    def add(cls, n: int, n1: int):
        return n+n1

    # If we don't care about other props then use static method

    @staticmethod
    def sub(n: int, n1: int):
        return n - n1


# sOb = StaticObject()
print(StaticObject.add(1, 2))
print(StaticObject.sub(1, 2))


class PlayerChar:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def run(self):
        print("run")


player1 = {"name": "vv", "age": 8}
p2 = PlayerChar("vbvb", 10)

print(player1)
print(p2.age)


# There is no True private in python
class PrivatePublic:
    def __init__(self, name: str):
        # Python programmers understood _<var name> as private
        self._name = name


a = PrivatePublic("Hey")


#  Inheritance
class User:

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("Do nothing")


class Wizard(User):

    def __init__(self, name, power, email="defaultmaile"):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power od {self.power}")


class Archer(User):

    def __init__(self, name, num_srrows):
        self.name = name
        self.num_srrows = num_srrows

    def attack(self):
        # User.attack(self)
        print(f"attacking with arrows {self.num_srrows}")


w1 = Wizard("mer", 50)
print(w1.sign_in())
a1 = Archer("ar", 100)
print(a1.sign_in())
print(w1.attack())
print(a1.attack())


print(isinstance(w1, Wizard))
print(isinstance(w1, Archer))
print(isinstance(w1, User))
print(isinstance(w1, object))


# Ploymorphism
def player_attack(char):
    char.attack()


player_attack(w1)
player_attack(a1)

# for char in [w1,a1]:
#     char.attack()

# Super
print(w1.email)

# introspection (Ability to determine the type of object at run time)
# print(dir(w1))

# Dunder methods
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.color}"
    
    # def __del__(self):
    #     print("deleted")
    
    def __call__(self):
        return ("call yes")

action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))

# del action_figure
print(action_figure())




class SuperList(list):

    def __len__(self):
        return 1000
    


sl = SuperList();
print(len(sl))
sl.append(5)
print(sl[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))


# Multiple Inheritance
class U:
    def seign_in(self):
        print("logged in")



class Wi(U):

    def __init__(self, name, power, email="defaultmaile"):
        # super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power od {self.power}")


class Ar(U):

    def __init__(self, name, num_srrows):
        self.name = name
        self.num_srrows = num_srrows

    def check_attack(self):
        # User.attack(self)
        print(f"attacking with arrows {self.num_srrows}")


    def run(self):
        print("ran really fast")
    
class HybridBorg(Wi,Ar):
    def __init__(self, name, power,arrows):
        Ar.__init__(self, name, arrows)
        Wi.__init__(self, name, power)



# hb = HybridBorg("name", 10)
# print(hb.run())

# hb = HybridBorg("boo", 10,100)
# print(hb.check_attack())


# MRO - Method Resoltion Order
class A:
    num = 10
    pass

class B(A):
    pass
    # num =11

class C(A):
    pass

class D(B,C):
    pass


print(D.num)
print(D.mro())