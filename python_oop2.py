#-*- coding: utf-8 -*-

class Myclass:
    var1 = "类的属性"
    def __init__(self):
        self.var1 = "对象的属性1"
        self.var2 = "对象的属性2"
    def func(self):
        print "对象的方法"
    func = classmethod(func)      # 将对象的方法变为类的方法
    def func2(self):
        print "对象的方法2"

print Myclass.var1
Myclass.func()
mys = Myclass()
print mys.var1
mys.func()
print Myclass.var1

#print Myclass.var2
#Myclass.func2()
