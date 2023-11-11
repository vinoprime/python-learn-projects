from time import time
print("Hello decors")


def performance(fn):
    def wrapper(*args, **kawrgs):
        start = time()
        result = fn(*args, **kawrgs)
        end = time()
        print(f"it took {end-start} s")
        return result

    return wrapper


@performance
def long_time():
    for i in range(50000000):
        i*5


long_time()
