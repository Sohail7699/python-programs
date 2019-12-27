class A():
    def __init__(self,name,address,salary ):
        self.name=name#public variable
        self.address=address #protected variable
        self.__salary=salary  #private variable


    def type(self):
        print(self.__salary)
        self.__salary=30000
        print(self.__salary)


class B(A):
    def __init__(self,name,address,salary):
        A.__init__(self,name,address,salary)

class C(B):
    def __init__(self):
        B.__init__(self,name,address,salary)


a=A('Sohail',"Kathmandu",3000)
b=B("bishnu","ratnapark",2000)
c=C()
