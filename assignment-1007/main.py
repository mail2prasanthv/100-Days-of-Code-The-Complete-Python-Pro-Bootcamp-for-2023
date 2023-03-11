#Method with positional and keyword argument
def greet_with(name, location):
    print("name:", name, " location:", location)


greet_with("prasanth", "London")
greet_with(name ="prasanth", location = "London")
greet_with(location = "London", name ="prasanth")

