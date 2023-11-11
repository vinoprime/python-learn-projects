print("Hello Error")


try:
    print(1+"4")
except:
    pass
    # print(f"Error=>>>")


try:
    print(1+"4")
    # print(1+4)
except ValueError:
    print("Value error")
except:
    print(f"Error=>>>")
else:
    print("Thank you")


def my_sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        print(err)


def my_sum(num1, num2):
    try:
        num1+num2
        10/0
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    finally:
        print("Finaly done")


def throw_error():
    raise ValueError("Hey cut it out")


print(my_sum(1, 2))
print(my_sum("1", 2))
throw_error()
