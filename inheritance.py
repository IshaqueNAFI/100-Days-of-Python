class Granfather:                                           #multi-level
    m= 10
    x=4
    y=5

    def sub(self):
        print(self.x-self.y+ Granfather.m)                                    #perent class

    def mul(self):
        print(self.x *self.y)



class Father(Granfather):
    pass


class Mother:
    a=100
    b=200

    def add(self):
        print(self.a + self.b)



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
      


       

    