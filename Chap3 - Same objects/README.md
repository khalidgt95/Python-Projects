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