#First class arguments - function name can be passed to a function as argument
def add (n1, n2):
    return n1+n2

def subtract (n1, n2):
    return n1 - n2

def divide (n1, n2):
    return n1 / n2

def multiply (n1, n2):
    return n1 * n2

def operation(function_name, n1, n2):
    return function_name(n1,n2)

print("pass add function as Argument:",operation(add, 10,5))
print("pass subtract function as Argument:",operation(subtract, 10,5))
print("pass divide function as Argument:",operation(divide, 10,5))
print("pass multiply function as Argument:",operation(multiply, 10,5))