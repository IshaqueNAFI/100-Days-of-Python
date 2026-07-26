class Granfather:                                           #multi-level
    m= 10
    x=4
    y=5

    def sub(self):
<<<<<<< HEAD
        print(self.x-self.y+ Granfather.m)      

    @staticmethod
    def addTwo ():
         print(Granfather.m + Granfather.y)                              #perent class
   
    def mul(self):
        print(self.x *self.y)

    def __init__(self):
            print("Granfatherather constractor")



class Father(Granfather):
    l=9
    p=8
    def __init__(self):
          print("Father's constrastor")

    def addFather(self):
             return self.l + self.p
=======
        print(self.x-self.y+ Granfather.m)                                    #perent class

    def mul(self):
        print(self.x *self.y)



class Father(Granfather):
    pass
>>>>>>> c80ee75a9d2b78ec8819b96a66fd0b1fb67ed2d2


class Mother:
    a=100
    b=200

    def add(self):
        print(self.a + self.b)

<<<<<<< HEAD
  





class son(Father):                                      #Multi -  inherit            #child class
    
    def __init__(self):
        super().__init__()           #to call father and son cons both
        print("son cosntractor")


    def addSon (self):
       sum =self.addFather()+100
       print(sum)
        


    @staticmethod
    def addThree ():
             print(Granfather.m + Granfather.x)   


obj = son()
obj.sub()
obj.mul()
obj.addFather()
obj.addSon()
print(obj.y)
print(obj.m)
obj1 = Father()
obj2= Granfather()


Granfather.addTwo()
son.addTwo()
Father.addTwo()
son.addThree()

obj3=Father()
obj3.addFather()









=======


class son(Mother,Father):                                      #Multi -  inherit            #child class
    pass



obj = son()
obj.sub()
obj.mul()
print(
obj.y)
print(obj.m)



obj1= son()
print(obj1.y)

obj1.sub()
obj1.add()
print(obj1.a)
      
>>>>>>> c80ee75a9d2b78ec8819b96a66fd0b1fb67ed2d2


       

    