class Person:
    def __init__(self,name,number,age):
        self.n=name
        self.no=number
        self.a=age
    def print(self):
        print(f"***Person Details***") 
        print(f"Name = ",{self.name})
        print(f"number = ",{self.number})
        print(f"Age = ",{self.age})
class Student(Person):
    def __init__(self, name, number, age,marks):
        super().__init__(name, number, age)  
        self.n=name
        self.no=number
        self.a=age
        self.m=marks
    def print(self):
        print(f"***Person Details***") 
        print(f"Name = ",{self.name})
        print(f"number = ",{self.number})
        print(f"Age = ",{self.age})
        print(f"Marks = ",{self.marks})
class Staff(Person):
    def __init__(self, name, number, age,experience):
        super().__init__(name, number, age,marks)
        self.n=name
        self.no=number
        self.a=age
        self.e=experience
    def print1(self):
        print(f"***Person Details***") 
        print(f"Name = ",{self.name})
        print(f"number = ",{self.number})
        print(f"Age = ",{self.age})
        print(f"Experience = ",{self.experience})
if __name__=='__main__':
    p1=input("Enter the name: ")
    p2=input("Enter the number: ")
    p3=input("Enter the age: ")
    p4=input("Enter the experience: ")
    p5=input("Enter the marks: ")
    obj.Staff(p1,p2,p3,p4)
