def add(a,b):
    try:
        s=a+b
    except:
        print("the value cannot be string")
    return s
def subtract(a,b):
    try:
        s=a-b
    except:
        print("the value cannot be string")
    return s
def multi(a,b):
    try:
        s=a*b
    except:
        print("the value cannot be string")
    return s
def divide(a,b):
    try:
        s=a/b
    except:
        print("the value is either 0 or string")
    return s


