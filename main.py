class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
    def introduce(self):
        print('Personal Info -->',self.name,self.age,self.gender)
        

p1 = Person("Bruno",26,'Male')
p1.introduce()
    