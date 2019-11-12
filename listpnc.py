prime=[]
a= int(input("enter the range"))
for i in range(2,a):
    z = True
    if (a%i) == 0:
        ans = False
        break
        prime.append(a)
print(prime)
