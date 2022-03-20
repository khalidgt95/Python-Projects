# Variable argument lists
* We can pass variable number of arguments using the following syntax:
```python
def func(*vals: str)    # vals is a tuple

    for v in vals:
        # Business logic
```
---
# Ways to pass arguments to functions
* We can use `*args` and `**kwargs` syntax to pass values
* The following example demonstrate this
```python
def func(arg1, arg2, arg3="THREE")
    return f"{arg1=}, {arg2=}, {arg3=}"

>>> vals = range(1, 2, 3)
>>> func(*vals)
'arg1=0, arg2=1, arg3=2'

>>> kw = {
    "arg1": "ONE",
    "arg2": "TWO"
}
>>> func(**kw)
"arg1='ONE', arg2='TWO', arg3='THREE'"
```
---
# Treating functions as objects
* In python, we can pass functions as arguments
* We can use the following syntax:
```python
def A(value: int) -> bool:
    ...

def B(value: int) -> bool:
    ...

def caller(*test: Callable[[int], bool]) -> None:
    test[0]()  # Call the function here

```
* We have to be careful about the order of functions we pass
* First function will be evaluated first, followed by other
--- 
# Monkey patching
* Assigning a function of a class to another function at runtime
```python
class A:
    def method_1():
        ...

def method_2():
    ...

def method_class_patch(self):
    ...
#  To patch a method of class
>>> obj = A()
>>> obj.method_1 = method_2
>>> obj.method_1()
# class method 2

# To patch a class method directly
A.method_1 = method_class_patch
```
* 