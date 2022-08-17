# object oriented programming

# class - a template (shape of a thing)
# attribute - a variable within a class
# method - a function within a class
# object - a particular instance of a class 
# constructor - code that runs whena an object is created (setting up the object)
# inheritance - the ability to extend a class to make a new class


# template, for Animal Class
class Animal: 
    # the data in the Class Animal
    x = 0 
    name = ""
    # constructor with parameter name
    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')
    
    # Method inside the class Animal
    def party(self): # passes it to self
        self.x = self.x + 1
        print("So far ",self.x)

    # destroy function
    def __del__ (self):
        print(self.name, ' destructed', self.x)

class Dog(Animal): # this is how you use inheritance
    age = 0
    def set_age(self):
        self.age = self.age + 7
        self.party()
        print(self.name, "points", self.age)



an = Animal("Paul") # Instance -> Animal object
an.party()
an.party()
an.party()

jk = Dog("Jeff")
jk.party()
jk.set_age()
jk.party()
print(jk.age)
