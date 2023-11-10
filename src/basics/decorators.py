print("Hello decors")

# @classmethod
# @staticmethod

def hello():
    print("Hellokjk")

greet = hello
del hello
print(greet())