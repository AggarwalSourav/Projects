class Square: 
    def __init__(self,side):
        self.s=side
    def area(self):
        ar=self.s*self.s
        print('Area of square',ar)
class Rectangle(Square):
    def __init__(self,len,br):
        super().__init__(len)
        self.l=len
        self.b=br
    def area1(self):
        super().area()
        ar1=self.l*self.b
        print('Area of Rectangle',ar1)
if __name__=='__main__':
    num1=int(input("Enter the first num:"))
    num2=int(input("Enter the second num:"))
    obj=Rectangle(num1,num2)
    obj.area1()
