import functools
from typing import Callable


def func_a(name: str) -> None:
    return f"hello {name}"

def caller(func: Callable, val: str) -> str:
    return func(val)

def parent():
    def child1():
        print(f"Inside child 1")

    def child2():
        print(f"Inside child 2")

    return child1


# Basic decorator example
def my_decorator(func: Callable):
    
    # We need this extra nested method because when we overwrite
    # the original function, the function argument list must 
    # match exactly the original function's argument list
    def wrapper():
        print(f"Start")
        func()
        print("End")

    return wrapper

# This method does not work as expected with a decorator
#
# def test(func: Callable):
#     print(f"Start")
#     func()
#     print("End")

#     return test

@my_decorator
def my_func():
    print("Inside business logic")

# ---------Passing arguments to decorator ------------#

def wrapper_execute_twice(func: Callable):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Inside wrapper")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print(f"Outside wrapper")
 
    return wrapper

# ---------Returning values from decorator ------------#
def wrapper_that_returns_value(func: Callable):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Inside wrapper")
        val = func(*args, **kwargs)
        print(f"Outside wrapper")
        return val
    
    return wrapper

@wrapper_execute_twice
def my_func_with_arguments(x, y, z):
    print(f" x = {x}, y = {y}, z = {z}")

@wrapper_execute_twice
def my_func_simple():
    print(f"I am in my_func_simple")

@wrapper_that_returns_value
def return_value():
    print(f"Inside return value")
    return "Returning value from return value"