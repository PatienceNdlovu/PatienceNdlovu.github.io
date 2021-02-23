def user_info(name, age, city):
    """This function is going to print name, age and city from argument provided"""

    print("{} is {} years old and lives in the city of {}!".format(name, age, city))


"""
I skipped two lines at the end of my function before beginning the next one as its a Python standard
"""
user_info("Patience", 37, "Leeds Leeds Leeds")


def user_info2(name, age=0, city="Leeds!"):
    """This function is going to put default values if the arguments do not provide an age or city"""
    print("{} is {} years old and lives in the city of {}!".format(name, age, city))


user_info2("Patience")
"""Entering just the name would have given an error. missing required positional argument"""
