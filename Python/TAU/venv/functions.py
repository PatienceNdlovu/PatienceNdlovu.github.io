"""
A function is a unit of code that can be reused throughout a program
starts with the letter def then a unique function name, the parenthesis and the colon
the body of a function is always indented 4 spaces and we remove the spaces when
we call the function
"""


# this is an example of what a hard coded function would look like

def addition():
    a = 15.7
    b = 45.2
    print(a + b)


# To see the results you need to call the function
addition()

# To create more flexibility for users

def addition2():
    a = int(input("Enter a number. "))
    b = int(input("Enter another number. "))
    print(a + b)


"""
I skipped two lines at the end of my function before beginning the next one as its a Python standard
"""
addition2()



