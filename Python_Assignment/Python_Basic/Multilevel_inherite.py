class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
class Dog1(Dog):
    def eat(self):
        print("Drinking")
    def cry(self):
        print("Crying")
obj=Dog1()
obj.eat()
obj.bark()
obj.cry()

#a=Animal()
#a.eat()