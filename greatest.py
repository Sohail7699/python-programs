a=input("enter the first no")
b=input("enter the second no.")
c=input("enter the third no.")
a=int(a)
b=int(b)
c=int(c)
if (a>b)and (a>c):
    print("A is greatest")
elif (b>a)and (b>c):
    print("B is greatest")
else:
    print("C is greatest")