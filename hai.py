class mySampleClass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)
x=mySampleClass()
y=mySampleClass()
x.hello("Anu")
x.print_name()
y.hello("Raju")
y.print_name()