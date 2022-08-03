class Ics:
    year=2020
    company="a"
    def __init__(self, name, age, place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def add_place(self, place):
        self.place=place
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
    @classmethod
    def add_company(cls,company):
        cls.company=company
    def display(self):
        print("Year is :",Ics.year)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Place :",self.place)
        print("Company :",Ics.company)

x=Ics("Anu",23,"MKD")
x.add_age()

x.add_place("PMNA")
x.add_year()
company=input("Enter a company name :")
x.add_company(company)
x.display()
