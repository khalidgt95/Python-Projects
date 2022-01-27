# Composition
* Composition means that an object is composed of other objects
* The composed object's lifespan depends on the main object.
    * Example is a chess board
    * It is composed of positions and chess pieces
### **Difference between composition and aggregation**
* Objects which can exist independently of main object are said to be in aggregate relationship
    * In a chess board, the chess pieces can exist without the chess board
    * But the chess positions cannot exist without the board
* In UML, **composition** relationship is represented as a **solid diamond**, while **aggregation** is represented as a **hollow diamond**
---
# Inheritance
* **is a** relationship
    * Orange **is a** fruit (Orange inherits from fruit)
* In UML, **hollow arrows** indicate that class **inherits** from the base class
---
## Duck typing
* Basic concept is that we do not check for the type of the object
* We just check if the class implements a certain method without worrying about the class types
    * Example is **len()** method in python
    * It can be called on lists, dicts and tuples
    * We do not care what is the object type as long as it contains this method
---
## Multiple Inheritance 
* Python has a **method resolution order** to define the function call order
* However, multiple inheritance can be substituted by composition
* In general, it should be avoided