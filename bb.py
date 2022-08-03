class Baseclass:
    def a(self,a,b):
        self.first=a
        self.second=b
        self.sum=self.first+self.second
class Subclass(Baseclass):
    def b(self):
        print("Entered numbers :",self.first,",",self.second)
        print("Sum is :",self.sum)

x=Subclass()
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
x.a(a,b)
x.b()