global_var=1

def someMethod():
    global global_var#making object "global_var" inside a method for updation using global variable
    global_var = global_var +1

someMethod()