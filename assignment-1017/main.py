#optional fields
def print_values(a=1, b=2, c=3): # a,b, c are optional
    print("a: ", a, " b: ", b, " c: ", c)


print_values()
print_values(10)
print_values(10,20)
print_values(10,20,30)
print_values(c=30)
print_values(a=10, c=30)
print_values(b=20)