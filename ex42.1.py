class Point(object):
    test = "hello"
    def sa(self, x):
        self.x = x
       
pt = Point()
pt.x = 20
print pt.x
print pt.test
