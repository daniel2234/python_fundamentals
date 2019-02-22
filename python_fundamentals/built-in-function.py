print("Whats your name?")
name = input()
print("Hello {}".format(name))

str(3)

int(5)

type("Bitmaker")

type(55)


# Defining functions

def my_first_function():
    return 1 + 1


my_first_function()

print(my_first_function())


def explicit_return_function():
    "The interpreter reads over me, but does nothing"
    return 25
    "The interpreter does not read me, because the return keyword above forces the interpreter to exit the function"
