class First:
    def disFirst(self):
        print("This is first")
class Second(First):
    def disSecond(self):
        print("This is second")
class Third:
    def disThird(self):
        print("This is third")
class Fourth(Second,Third):
    def disFourth(self):
        print("This is fourth")
x=Fourth()
x.disFirst()
x.disSecond()
x.disThird()
x.disFourth()
print(Fourth.mro())