import math

class shape:
    def __init__(self):
        self.area=0
        self.name=" "

    def display(self):
        print("the area of the",self.name,"is:",self.area,"units")

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        self.area=0
        self.name="cirle"

    def calc_area(self):
        self.area=math.pi*(self.radius**2)

class tri(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        self.area=0
        self.name="Triangle"

    def calc_area(self):
        self.area=(1/2)*self.base*self.height

class rect(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=0
        self.name="rectangle"

    def calc_area(self):
        self.area=self.l*self.b

c1=circle(10)
c1.calc_area()
c1.display()

t1=tri(10,10)
t1.calc_area()
t1.display()

r1=rect(10,10)
r1.calc_area()
r1.display()


