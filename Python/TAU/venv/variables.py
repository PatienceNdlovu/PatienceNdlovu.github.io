# this is a single line comment in python!!!
# Always make sure the variable names are descriptive
# variables in python can start with underscores or without and are case sensitive.

_patience = "female"

patience = "girl"

PATIENCE = "woman"

print(_patience)
print(patience)
print(PATIENCE)

"""
This is a multi line comment - 3 quotes to start and 3 quotes to finish. 
This is really useful for docstrings when you are writing long lines of code.
"""

name = "Patience Ndlovu"
type_of_car = "Ford Fiesta"
school = "Test Automation University"

# The line below will print the two variables together without any spaces
print(name + school)

# Option 1 to fix, we can add a space by adding quotes and an actual space like below, but it is still not the best!
print(name + " " + school)

"""
Option 2 we can use python formatting method
uses curly braces in each of the places that i would put variables
the method accepts the arguments of our variables and transfers those arguments into curly braces
"""
print("{} works at {}.".format(name, school))