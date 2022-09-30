# defining a function

def add(arg1, arg2):
    total = arg1 + arg2
    return total

# default value
def greetings(msg="morning"):
    print(f"Good {msg}")

greetings("night")

# variable lenght arguments
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for i in args:
        print(f"You have also ordered {i}")

order_food("pizza", "coke", "cake")