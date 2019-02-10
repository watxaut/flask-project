import functools


# Step 1
def parent(name):
    print("Printing from the parent() function")

    # this function is not visible from the file scope
    def first_child():
        print("Printing from the first_child() function")
        print("Also, printing name: {}".format(name))

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent(name="Joan")

try:
    first_child()  # this will give an error
except:
    print("first_child() does not exist in project scope")


# Step 2 - Passing a function to a function (inception)
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
say_whee()  # boom


# Step 3 - Do it with python syntax
@my_decorator
def say_woo():
    print("Woo!")


say_woo()


# Step 4 - Advanced decorators
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def say_something(sentence):
    print(sentence)


say_something("Hey there")  # will print Hey there twice


# Function that returns
def dec_returns(func):
    def wrapper(*args, **kwargs):
        print("I do something before")
        aux_out = func(*args, **kwargs)
        print("I do something after")
        return aux_out
    return wrapper


@dec_returns
def los_hahas():
    return "LOL"


a = los_hahas()
print(a)


# __name__ of the functions not matching wtf  --> functools.wraps
def do_3_times(func):
    @functools.wraps(func)
    def wrapper_do_3_times(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_3_times


# Real case examples:

# timing function
# debug function
# do something before or after function
# slowing down code
# Flask ;)

# more in:  https://realpython.com/primer-on-python-decorators/
