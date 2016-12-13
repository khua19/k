class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return (self.r**2)*3.141592
    def circumference(self):
        return self.r*2*3.141592
x=Circle(500)
print x.area()
print x.circumference()
