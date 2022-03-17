# NamedTuple
* Since indexing in normal tuples can be confusing, we can use NamedTuple
* It works the same as tuple but maps values to variables
* Advantage is that we can add behaviour to the data like normal class 
---
# Dataclasses
* They let us define attributes in a easy-to-use manner
* Acts as a placeholder for a set of related attributes
* We don't need to write a constructor
---
# Dictionaries
* They are the key-value data structure
* The key can be anything as long as it is hashable
---
# DefaultDict
* It is the same as a `dict` but accepts a function in the constructor
* When a key is not present when called, it returns this function and creates the key
* The generic syntax is as follows:
```python
from collections import defaultdict

var = defaultdict(<Any_class>)  # This can be int, float or custom defined class
```
---
# Counter
* It is another class which counts the instance of the input
* It has many methods which can be used such as shown below:
```python
>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15
```
---
# Sorting Lists
* We can use the `sort()` method of list to sort primitive datatypes
* To sort a list of objects, the object must implement the `__lt__()` method
* The basic structure to do this is as follows:
```python
class A:

    val: int

    def __lt__(self, other: Any): # Any so that we can use ducktyping for object of other classes
        return self.val < other.val
```
* To sort on a specific attribute, we can do the following:
```python
>>> import operator
>>> file_list.sort(key=operator.attrgetter("name"))
```
--- 
