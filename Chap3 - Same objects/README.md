# Instance and class variables
* Consider the following piece of code:
```python
class Contact:
    all_contacts: List["Contact"] = []

    def __init__(
        self, 
        name: str, 
        email: str
    ) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

```
* Here, the variable ```all_contacts``` is a class variable, which is shared among all the instances of the class
* It is more like a global variable which can be read and write by all of the instances of this class
* In contrast, the variables declared inside the constructor are instance variables
---
# Extending built-in types
* We can inherit from built-in datatypes the same way we inherit normal classes
* The datatype will still behave normally
* Useful when it makes sense that the functionality should be done by the built-in datatype
* Consider the following example which extends the ```dict``` class 
```python
class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        longest: Optional[str] = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest
```
---
# Multiple Inheritance
## Mixin
* It is a class definition which does not exist by itself but provides additional functionality to the inheriting classes
* Useful when a single functionality needs to be shared across different classes 
* 