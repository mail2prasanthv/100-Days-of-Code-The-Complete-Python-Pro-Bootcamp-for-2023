# variable scope
global_scope_variable=100

def samplemethod():
    #print("Inside method:",global_scope_variable) #-- Error here using undeclared variable -- UnboundLocalError: local variable 'global_scope_variable' referenced before assignment
    global_scope_variable = 200#Actualy local variable
    print("Inside method:",global_scope_variable)
    
print("Outside method:",global_scope_variable)
samplemethod()
print("Outside method:",global_scope_variable)