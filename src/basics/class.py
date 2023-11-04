


class BigObject:

    def __init__(self, name):
        self.name = name

    def printHello(self, name: str):
        print(f"Hello {name}")

    def printName(self):
        print(self.name)


obj = BigObject("Vinoth")
obj1 = BigObject("Rag")

obj.printName()
obj1.printName()