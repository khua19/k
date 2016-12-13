class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius**2)*3.14

    def perimeter(self):
        return 2*self.radius*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.radius, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return (2* self.x) + (2 * self.y)

    def __str__(self):
        return "Rectangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x


class Triangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h=(x**2+y^2)**.5
    def area(self):
        return (self.x*self.y)/2

    def perimeter(self):
        return self.x+self.y+self.h

    def __str__(self):
        return "Triangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

x = Triangle(3,7)
print x
y = Triangle(5,9)
print y

class Isosceles(Triangle):
    def __init__(self, x):
        self.x = x
        self.y = x
x = Triangle(3,7)
print x
y = Triangle(5,9)
print y




class Depth():
    def __init__(self, z):
        self.z=z
    def volume(self):
        return self.area()*self.2
    def sa(self):
        return 2*self.area+self.2+self.perimeter
