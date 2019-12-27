#use exception handling to report out of bound error  a=[1,2,3] then    print(5)   // gives error now use try catch to handel these errors
a = [1, 2, 3]
b = [1, 4, 0]
try:


    for i in range(len(a)):
        print(a[i]/b[i])
    print(a[5])
except(ZeroDivisionError,IndexError):
    print('out of range')