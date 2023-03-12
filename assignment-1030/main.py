#First class arguments - function name can be passed to a function as argument
def add (n1, n2):
    return n1+n2

def subtract (n1, n2):
    return n1 - n2

def divide (n1, n2):
    return n1 / n2

def multiply (n1, n2):
    return n1 * n2

def operation(symbol, n1, n2):
    function_name = get_function_name(symbol)
    return function_name(n1,n2)

def get_function_name(symbol):
    if(symbol == "+"):
        return add
    if(symbol == "-"):
        return subtract
    if(symbol == "/"):
        return divide
    if(symbol == "*"):
        return multiply

print("pass add function as Argument:",operation("+", 10,5))
print("pass subtract function as Argument:",operation("-", 10,5))
print("pass divide function as Argument:",operation("/", 10,5))
print("pass multiply function as Argument:",operation("*", 10,5))