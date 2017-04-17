# class Employee
#
# # methods
# eat()
# eat(food="sandwich")
# eat(companions=[Sam, Dean, Alice])
#     SELECT * FROM restaurant
#     #deserialization to select from strings
# eat("pizza", [Sam, Dean, Alice])
#
# #!/usr/bin/env python

class Employee:
    def getEmployee(self, food=None, name=None, restaurant=None):
        if food is not None and name is not None and restaurant is not None:
            print(food + name + restaurant)
        elif name is not None and food is not None:
            print('Please assign a restaurant')
        elif name is not None and restaurant is not None:
            print('Please assign a food')
        else:
            print('You have no employees to eat with ')

# Create instance
myEmployee = employee()

# Call the method
myEmployee.eat()
# Call the method with a parameter
myEmployee.eat(food='pizza')
myEmployee.eat(name=[Sam, Dean, Alice])
myEmployee.eat(restaurant='Applebees')
