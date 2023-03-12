def outer_function():
    print("I am outer")
    
    def nested_function(): #nested function
        print("I am nested")

    nested_function()


# nested_function() can't be called directly 
outer_function()
