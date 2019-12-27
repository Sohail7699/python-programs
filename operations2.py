def add(a,b):
    try:
        c=float(a)+float(b)
    except:
        print('Value can not be string')
    return c

def subtract(a,b):
    try:
        c=float(a)-float(b)
    except:
        print('Value can not be string')
    return c

def multiply(a,b):
    try:
        c=float(a)*float(b)
    except:
        print('Value can not be string')
    return c

def divide(a,b):
    try:
        c=float(a)/float(b)
    # except(b):
    #     if float(b)!=0.0:
    #         print('Value can not be string.')
    #     else:
    #         print('Value of b can not be 0.
    except:
        print('Error! Value can not be string or value of b can not be 0. Please check and enter again.')
    return c
