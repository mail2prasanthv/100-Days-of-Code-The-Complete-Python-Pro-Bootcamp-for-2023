#no block scope

def samplemethod(mark):
    if mark>10:
        grade="A"
        newgrade="D"

    if mark <50:
        grade="B"
        newgrade="C"
    #no block scope in python
    print(grade)#variable introduced inside an "if" block- still accessible outside
    print(newgrade)#variable introduced inside an "if" block- still accessible outside

samplemethod(50)