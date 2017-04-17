# bangazon-03-methodoverloading
Method overloading in Python uses a single method, but utilizes parameter names and default values. This allows a single method to have multiple signatures.

Bangazon Orientation - Method Overloading

Method overloading in Python uses a single method, but utilizes parameter names and default values. This allows a single method to have multiple signatures.

Instructions

Create a new class to represent an Employee.

It's constructor should accept two parameters.

First name of employee
Last name of employee
Define a method named eat() that will allow it to be invoked with the following four signatures.

eat() - Will select a random restaurant name from a list of strings, print to console that the employee at at that restaurant, and also return the restaurant.
eat(food="sandwich") - Will output that the employee ate that specific food at the office.
eat(companions=[Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and also output the first name of each employee in the specified list.
eat("pizza", [Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and ordered the specified food, with the first name of the teammates specified in the list.
Note: Notice that this signature doesn't require that the parameters to be named
