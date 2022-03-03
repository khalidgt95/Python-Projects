# Exceptions
* The general way to raise an Exception is as follows:
```python
def func() -> NoReturn:
    print("Raising an exception now")
    raise RuntimeError("Runtime error encountered")
```
# try-except clause
* To handle an exception, we can use the ```try-except``` clause
```python
def exception_raiser() -> NoReturn:
    raise RuntimeError("Runtime error")

def handler() -> None:
    try:
        exception_raiser()
    except Exception as ex:
        print(f"Exception caught")
    print("Exiting function")

"""
Output

>>> handler()
Runtime error
Exception caught
Exiting function

"""
```
* If we want to handle multiple exceptions, we can use the following syntax:
```python
def division_with_errors(value: int) -> Union[str, float]:
    try:
        if value == 10:
            raise ValueError("10 not allowed")
        
        return 100 / value

    except ZeroDivisionError:
        return "0 not allowed"
    except TypeError:
        return "only numbers allowed"
    except ValueError:
        print("10 not allowed")
        raise # Raises the value error again
    except Exception:
        print("Catches all the other exceptions")
```
* One thing to remember is that the ```finally``` block is always executed, even when no exception is raised
* Never use the ```except``` clause directly to catch the exception like shown below
```python
def call():
    try:
        ...
    except: # never do like this
        ...
```
# Where it makes sense to use try clause
* If there is a piece of code where you think that something can go wrong due to any reason, it's better to wrap it into ```try``` block
* Advantage is that you do not need to check for all the edge cases that can arise
# Creating your own exceptions
* We can inherit from the ```Exception``` class as shown below
```python
class MyCustomException(Exception):
    pass
```
* The custom exception behaves like any other exception
```python
def call():
    raise MyCustomException("Specific problem exception")
```
* The class name should define what the exception is about
# Importance of Exceptions
* It can serve as a way to convey context information between two components
* The caller can behave differently based on the type of exception encountered