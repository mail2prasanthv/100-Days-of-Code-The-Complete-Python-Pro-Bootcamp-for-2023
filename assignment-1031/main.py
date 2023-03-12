# Decorators
#Manual Decorators
#Code to log the time taken to execute a function
# the existing function is wrapped with some codes to log the time

import time

def decorator_function(actual_function_name):
    
    def nested_function(elements, to_be_searched):
        start_time = round(time.time()*1000) #pre
        
        actual_function_name(elements, to_be_searched) #calls search method
        
        end_time = round(time.time()*1000) #post
        print("Total Time taken:" , (end_time - start_time))
    
    return nested_function

def search(elements, to_be_searched):
    found = False
    time.sleep(3)
    for element in elements:
        if to_be_searched == element:
            found= True
    return found

mylist = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]

decorated_nested_function  = decorator_function(search)#passing function to be decorated as an argument
decorated_nested_function(mylist, 5)