class Student:
    # def __init__ (self) to jest konstruktor
    #do tego odwołujemy się self'em
    #def metody (self,...)
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def increase_age(self):
        self.age += 1
s1 = Student("Piotr",0,24)
print(s1.age)
s1.increase_age()
print(s1.age)
s2 = Student("Roman",1,20)
print(s2.name,s2.age)