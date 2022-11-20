class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name:",self.name,"\n","Age:",self.age)
class update(student):
    def call(self):
        self.details()
obj=update("Sanjay",20)
obj.call()
