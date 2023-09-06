import math


class shape:
    '''base class'''

class triangle(shape):
    def get(self):
        self.a=float(input("enter side a:"))
        self.b = float(input("enter side b:"))
        self.c = float(input("enter side c:"))
        self.s=(self.a+self.b+self.c)/2
    def area(self):
        area=math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        print("area of triangle is:",area)



class rectangle(shape):
    def get(self):
        self.a=float(input("enter side a:"))
        self.b = float(input("enter side b:"))


    def area(self):
        area=self.a*self.b
        print("area of rectangle is:",area)


class circle(shape):
    def get(self):
        self.r=float(input("enter radius:"))



    def area(self):
        area=self.r * self.r * 3.14
        print("area of circle is:",area)

c1=triangle()
c2=rectangle()
c3=circle()

c1.get()
c1.area()

c2.get()
c2.area()

c3.get()
c3.area()