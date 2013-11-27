## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):
   
    def __init__(self, name):
        ##??
        self.name = name
        print '%s is a dog' % self.name  
##??
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print '%s is a cat' % self.name


##??

class Person(object):
 

    def __init__(self, name):

        self.name = name      
     
        self.pet = None
        
    def printpet(self) :

    	print '%s is a human, and his pet is %s' % (self.name, self.pet.name)
##??
class Employee(Person):

    def __init__(self, name , salary):

        super(Employee, self).__init__(name)
        self.salayr = salary

##??
class Fish(object):
    pass



class Salmon(Fish):
    pass

class Halibut(Fish):
    pass




rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

mary.printpet()

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
print mary.pet

