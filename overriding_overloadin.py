class Father:
    x=4
    y=5

    def add(self):
        print(self.x+self.y)



class son (Father):
    def add1 (self,a=0,b=0):                  #default argument parameter
        print(self.x +self.y+1+b+a)




    def myMethod(self,*a):     #variable lenght argument  ( unkinted value passs)
        print(a)


    


obj1= son()
obj1.add1(4)
obj1.add1()
obj1.add1(3,4)
obj1.myMethod(3,3,3,4,3,2,3,4,4,4,3,3)
obj1.myMethod(1,3)
obj1.myMethod()

