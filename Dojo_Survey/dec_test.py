def add_5(func_arg):
    print("Decorator function has been declared")
    def inner1(*args, **kwargs):
        print("initiating inner function to call native function")
        result1 = func_arg(*args, **kwargs)
        print(f"Inner function ran native function and got {result1}")
        result = result1 + 5
        print(f"The inner function is doing the work of the decorator and adding 5 to the previous result")
        return result
    print("After the inner function and just before the return line")
    return inner1

@add_5
def mult5(a):
    print(f"accepted {a} into the native function")
    result = a*5
    print(f"native function will return {result}")
    return result

# print(mult5(4))

def logged_in(func_arg):
    if bool == False:
        print("User not logged in")
        return
    else:
        def inner1(*args, **kwargs):
            return func_arg(*args, **kwargs)
        return inner1

@logged_in
def users_only(stuff_to_do):
    print(f"the user {stuff_to_do}")
    return

users_only("logged in, changed data")

users_only("not logged in, changed data")

