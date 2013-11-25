"""Python面向对象初级教程 2010-01-11 17:01:56

分类： Python/Ruby
"""
'''
    python不单单用作结构化编程，她还是面向对象的高级语言，支持类(class)，本文将介绍Python面向对象的编程思想。类(class)被用来用户自定义数据类型，用户使用类(class)来组织数据，管理数据。
    类(class)的定义
    类(class)的属性(attribute)
    类(class)的方法(method)
    类(chalss)成员的控制域
    类(class)的继承与组合
1.类的定义，类的定义使用关键字class，后跟类的名称，及":"。如定义一个Point类
'''
# 定义一个空的类，没有任何属性与方法
class Point:
    pass
'''
向类中添加类属性(有的称之为类成员)，类属性与其它的变量使用方法一致，第一次使用便是对此变量的定义，属性的作用域为整个类，即这个类的所有方法可以访问此属性，定义Point属性的属性x和y
'''
# 定义一个空的类，没有任何属性与方法
class Point:
    # 定义x和y坐标
    x = 10
    y = 10

'''
类方法为特殊的函数，其定义方法与函数类似，但有一个默认的参数self，表示此类对象的实例(instance)，定义类的方法，设置x的方法setX和获取x的方法getX。
'''
# 定义一个完整的类，包含属性与方法
class Point:
    # 定义x和y坐标
    x = 10
    y = 10
    def setX(self,x_):
        self.x = x_
    def getX(self):
        return self.x
    def setY(self,y_):
        self.y = y_
    def getY(self):
        return self.y
    def setXY(self,x_,y_):
        self.setX(x_)
        self.setY(y_)
'''
注意：这个类方法如何访问类属性，使用self.x，而不是x。python类方法与C++不同，类的成员方法不会自动使用类的属性，必须使用self明确指定。如果只使用x，则在setX函数中创建了一个变量x，并将其值设置为_x。
    同样对于类方法之间互相访问时也必须使用self指定为调用的为类的方法。
'''
# python还支持在类定义块之外定义方法，这个方法满足类方法，例如先定义一个函数outX
def out_setX(self,x_):
    self.x = x_
# 然后定义类，并将类成员h赋值为out_setX
class Point:
    x = 10
    y = 10
    setX = out_setX
'''
创建一个类的对象,并访问这个类的属性和方法
'''
# 创建Point的一个对象
pt = Point()
# 设置坐标x的值
pt.x = 10
# 获取坐标x的值
print pt.x
# 访问对象的方法
pt.setX(20)

'''
    C++中有函数重载的概念，python则没有，如果有如下函数定义
def f():
    print 'f'
def f(x):
    print 'f(x)'
f()
f(20)

出错信息
TypeError: f() takes exactly 1 argument (0 given)
由于f先定义为无参数的函数，后有定义为带一个参数的函数，及f被重新定义，所以再次调用
f()时，解释器抱怨找不到无参数名称为f的函数。但可以使用如下
def f():
    print 'f'
def f(x):
    print 'f(x)'
#此id已被重新定义，可以这样解释：
##    x = 10
## x = 20
#此时x的值已经被改编为20，已不再是10无法在访问10
#f()
f(20)
'''
'''
    C++还有构造函数(constructor)的概念,这个函数为一特殊的函数，在创建对象时自动被调用，python中也没有构造函数，有一个功能类似的函数，用来初始化类属性，这个函数为：
__init__，如下代码，在创建对象时将类属性初始化
'''
class Point:
    x = 10
    y = 10
    def __init__(self,x_,y_):
        self.x = x_
        self.y = y_

# 将坐标(x,y)设置为(20,20)        
pt = Point(20,20)
print pt.x,pt.y

'''
类的成员(属性和方法)，python默认使用public，即属性与方法可以被直接访问，这一点与C++也不相同，python改变属性可见性的是通过表示ID，私有成员以"前导字符_至少两个，后尾字符_最多一个"表示，如定义私有属性和私有方法
私有属性：
    __pri1        前导字符个数2
    ___pri2        前导字符个数3
    ____pri3_    前导字符个数4，后尾字符1
共有属性：
    _pub1        前导字符1
    ___pri2__    前导字符3，后尾字符2
'''
class Point:
    # 私有属性，只能通过类方法访问
    __x = 10
    # 私有方法，可被其他类方法调用
    def __setX(self,x_):
        # 访问私有属性
        self.__x = x_
    def setX(self,x_):
        # 调用私有方法
        self.__setX(x_)
    def getX(self):
        # 访问私有属性
        return self.__x
pt = Point()
# 直接访问__x
# pt.__x
# 解释器会抱怨没有__x属性
# AttributeError: Point instance has no attribute '__x'
# 访问私有方法
# pt.__setX(10)
# 解释器还是会抱怨没有属性__setX(python视方法也为属性)
print pt.getX()
pt.setX(20)
print pt.getX()

'''
在类中可以定义属性，有此类创建的对象可以使用此类的所有属性，除此之外，python还支持动态向类或类对象中添加属性。向类中添加属性，其后所有的类对象便可以使用新添加的属性；若向类对象中添加属性，只用此类对象可以使用此属性
'''
'''向类中添加属性'''
class Point:pass

# 向类中添加属性z
Point.z = 30
# 创建类对象
pt = Point()
pp = Point()
# 访问类属性z
print Point.z
# 访问类对象属性z,pp与pt均含有属性z
print pt.z,pp.z

'''向类对象中添加属性'''
class Point:pass

pt = Point()
pp = Point()
# 向类对象中添加属性
pt.z = 10

# 访问类的属性
# print Point.z
# 解释器抱怨没有属性z
#AttributeError: class Point has no attribute 'z'
print pt.z

# 访问pp对象的属性z
# print pp.z
#解释器抱怨没有z属性
#AttributeError: Point instance has no attribute 'z'

'''
类的继承与组合，实现代码重用。不用copy&paste代码，当创建新类时，不必全部从头开始，尽可能的使用已有代码。TIC++中使用两种方法:一种称为组合(composition)；另一种称为继承(inheritance)。
继承语法格式：
class class DerivedClassName(BaseClassName):pass
'''
'''子类访问父类属性'''
class Point:
    x = 10
    y = 20
    def setX(self,x_):
        self.x = x_
    def getX(self):
        return self.x
    
class Circle(Point):
    r = 5
# 创建父类对象
pt = Point()
# 创建子类对象
cl = Circle()
# 访问父类的属性
print cl.x,cl.y
# 访问父类的方法
cl.setX(40)
print cl.x,cl.y

'''重载父类属性，访问Circle属性'''
class Point:
    x = 10
    y = 20
    def setX(self,x_):
        self.x = x_
    def getX(self):
        return self.x
    
class Circle(Point):
    x = 40
    y = 50
    r = 5
# 创建父类对象
pt = Point()
# 创建子类对象
cl = Circle()
# 访问Circle类的属性
print cl.x,cl.y
# 40,50

'''重载父类属性，访问父类Point属性'''
class Point:
    x = 10
    y = 20
    def setX(self,x_):
        self.x = x_
    def getX(self):
        return self.x
    
class Circle(Point):
    x = 40
    y = 50
    r = 5
    # 访问父类的属性
    def callBase(self):
        # x,y已经被Circle重载，显示使用父类访问父类属性
        print Point.x,Point.y
# 创建子类对象
cl = Circle()
# 访问Point类的属性
cl.callBase()
# 10,20

'''
C++语言中的子类会自动调用父类的构造函数，python中的__init__不会自动调用父类的__init__，如果要调用必须显示的调用父类的__init__
'''
'''重载父类属性，访问父类属性'''
class Point:
    def __init__(self):
        print 'Point'
    
class Circle(Point):
    def __init__(self):
        # 显示调用父类的__init__函数
        Point.__init__(self)
        print 'Circle'
cl = Circle()
# Point
# Circle
'''
C++有抽象类，此类只定义函数接口(有的称之为interface)，其具体的实现有子类来实现，python没有抽象类，实现方法：将基类函数接口设置为None，如果使用此基类创建对象，调用此函数时会出现异常，具体实现由其子类实现
'''
#抽象类
class Graphic:
    draw = None
# 实现Graphic的draw
class Point(Graphic):
    x = 10
    y = 10
    # 将draw赋值
    def __init__(self):
        self.draw = self.__draw
    # 实现抽象接口
    def __draw(self):
        print self.x,self.y
# 实现Graphic的draw
class Circle(Point):
    r = 5
    # 将draw赋值
    def __init__(self):
        self.draw = self.__draw
    # 实现抽象接口
    def __draw(self):
        print self.x,self.y,self.r
# 创建各个类的对象
gp = Graphic()
pt = Point()
cl = Circle()
#gp.draw()
# 函数调用出错
#TypeError: 'NoneType' object is not callable
# 调用Point的draw
pt.draw()
# 调用Circle的draw
cl.draw()

'''
类的组合：类的另一种重用方式，《C++ Primer plus》有介绍适用于此设计方法的类与类之间的关系，称之为”has-a“关系，与继承”is-a“关系相对应。
”is-a“关系：
圆柱(cylinder)is-a特殊的圆(circle)，它含有高度属性，圆(circle)为圆柱(cylinder)的父类;
圆(circle)is-a特殊的点，它含有半径属性,点(point)为圆(circle)的父类
'''
# 定义父类及子类
class Point:pass
class Circle(Point):pass
class Cylinder(Circle):pass

'''
”has-a"关系：
画布(canvas)上可以绘制各种图形(如：点(point)、圆(circle)和圆柱(cylinder)等)。绘图程序
定义如下关系
'''
# 定义容器类
class Canvas:
    # 包含三个类对象Point、Circle和Cylinder
    pt = Point()
    cl = Circle()
    cy = Cylinder()
    def __init__(self):
        pass 
