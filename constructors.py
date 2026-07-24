class Myclass:
    x=3
    y=4

    #m=6


    def __init__(self,a,b,z, xValue):
        self.m = z   #instant variable

        self.x=xValue    #value changed

        sum=self.x+self.y+a-b+z
        print(sum)
        print("hello constructor")


    def classTwo(self):
        print(self.x+self.y+self.m)



obj=Myclass(2,1,6,99)

print(obj.x)     
print(obj.m)
obj.classTwo()
