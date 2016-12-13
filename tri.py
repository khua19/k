class rightTriangle():
    def __init__(self,side):
        self.s=side
        self.h=(2(side^2))^.5
    def area(self):
        return (self.s^2)/2
    def perimeter(self):
        return self.s*2+self.h

x=rightTriangle(20)
print x.area()
print x.circumference()
