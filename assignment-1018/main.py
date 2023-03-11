# Unlimited arguments
def test_unlimited_args(*args):
    for item in args:
        print(item)

test_unlimited_args(1,2,3,4)