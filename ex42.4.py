class Person():
    number = 10
    def __init__(self, number):
        self.number = number
        print self.number
        print Person.number
        print self.number

class Point():
    test = "This is a ..."
    x = 10
    y = 20

    def setX(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

p = Person(20)
print p.number

pt = Point()
pt.setX(1, 2)

print Point.x, Point.y
print pt.x,pt.y,pt.test, pt.getX(), pt.getY()

