# Object and Classes

* **Object** is a collection of data with associated behaviours
* Objects can be associated with each other
* **Classes** are the blueprints for creating an object
---

* When we design a system, we try to figure out what objects need to be created and how they should interact with each other
* This process is called **OOAD**
---

# Interfaces
* Interface is a collection of attributes and methods that other object can use to interact with that object
    * A simple example is a television. 
    * The interface for TV is the remote control
    * As a user, we do not care what are the internal workings as long as it does what it's supposed to do
* This process of hiding information is called **Information Hiding** or **Encapsulation**
* **NOTE:** Interfaces should **not** be chaged frequently since it can lead to breaking changes to all the things that depend on it
---
# Abstraction 
* Level of detail that is exposed to the outside world
* Some classess need to access small parts of the object attributes while other need to access a lot of attributes
    * Consider the car as the object
    * The driver needs access to only steering wheel and pedals
    * While the mechanic needs to access more attributes
    * Thus there are different levels of abstraction to different objects
