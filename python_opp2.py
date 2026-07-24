class Myclass:
    x=2  #classs variable
    y=8
    z=4
    def addTwo(self,a,c):      

        sum2 =self.x +self.y +a
        print("sum2 result",sum2)


    def addNew(self):
            self.addTwo(6,6)



obj = Myclass()
obj.addTwo(10,10)
obj.addNew()








    
"""

obj1 = Myclass()
print(obj1.x)
print(obj1.sum)


obj2=Myclass()
print(obj2.y)



obj3=Myclass()
print(obj3.z)
"""


