import operations
try:
    a=float(input("enter a"))
    b=float(input("enter b"))
    print(operations.add(a,b))
    print(operations.subtract(a,b))
    print(operations.multi(a,b))
    print(operations.divide(a,b))
except:
    print("it is string")

