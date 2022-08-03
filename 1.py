class calculation:
    def sum(self):
        print("Find sum")
        a=int(input("first number :"))
        b=int(input("second number :"))
        sum=a+b
        print("Sum=",sum)
    def dif(self):
        print("Difference")
        a=int(input("first number :"))
        b=int(input("second number :"))
        dif=a-b
        print("Difference=",dif)
    def mul(self):
        print("Multiplication")
        a=int(input("first number :"))
        b=int(input("second number :"))
        mul=a*b
        print("Product=",mul)
    def div(self):
        print("Division")
        a=int(input("first number :"))
        b=int(input("second number :"))
        div=a/b
        print("Division=",div)

x=calculation()
x.sum()
x.dif()
x.mul()
x.div()