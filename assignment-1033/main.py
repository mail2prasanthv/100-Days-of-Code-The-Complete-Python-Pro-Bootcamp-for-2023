# Decorators
#Decarators with @
#Code to log the time taken to execute a function
# the existing function is wrapped with some codes to log the time
#Instead of assigning the function call to a variable, 
# Python provides a much more elegant way to achieve this functionality using the @ symbol. For example,
import time

def decorator_function(actual_function_name):
    
    def nested_function(*args, **kwargs):
        start_time = round(time.time()*1000) #pre
        print("First element: " , args[0])
        print("Second element: " , args[1])
        actual_function_name(args[0], args[1]) #calls search method
        
        end_time = round(time.time()*1000) #post
        print("Total Time taken:" , (end_time - start_time))
    
    return nested_function

@decorator_function
def search(elements, to_be_searched):
    found = False
    time.sleep(3)
    for element in elements:
        if to_be_searched == element:
            found= True
    return found

mylist = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]
search(mylist,5)