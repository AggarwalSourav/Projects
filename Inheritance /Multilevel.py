class Square: 
    def __init__(self,side):
        self.s=side
    def area(self):
        ar=self.s*self.s
        print('Area of square:',ar)
class Rectangle(Square):
    def __init__(self,len,br):
        super().__init__(len)
        self.l=len
        self.b=br
    def area1(self):
        super().area()
        ar1=self.l*self.b
        print('Area of Rectangle:',ar1)
class Box(Rectangle):
    def __init__(self,len,br,height):
        super().__init__(len,br)
        self.l=len
        self.b=br
        self.h=height
    def area2(self):
        super().area1()
        ar2=self.l*self.b*self.h
        print("Area of Cube:",ar2)
if __name__=='__main__':
    num1=int(input("Enter the first num:"))
    num2=int(input("Enter the second num:"))
    num3=int(input("Enter the third number:"))
    obj1=Box(num1,num2,num3)
    obj1.area2()
