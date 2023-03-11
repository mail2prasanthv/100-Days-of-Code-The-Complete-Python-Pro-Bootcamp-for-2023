# keyword argument
# Unlimited arguments
#using dictionary
def test_unlimited_args(**kwargs):
    print("Type:", type(kwargs))
    
    for key,value in kwargs.items():
        print(key,":", value)

test_unlimited_args(firstname="prasanth",lastname="varghese")