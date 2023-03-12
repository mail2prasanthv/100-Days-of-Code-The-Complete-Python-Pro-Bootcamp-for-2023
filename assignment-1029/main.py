#Outer function returning the refereces of nested function
# A function can return a function
def outer_function():
    print("I am outer")
    
    def nested_function(): #nested function
        print("I am nested")

    return nested_function# returning the references of nested_function


# nested_function() can't be called directly 
nested =  outer_function()
nested()
