class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name:",self.name,"\n","Age",self.age)
class student2:
    def fun(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name:",self.name,"\n","Age:",self.age)
class student3(student,student2):
    def fun(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name:",self.name,"\n","Age:",self.age)
obj=student3("sanjay","20")
obj.details()
