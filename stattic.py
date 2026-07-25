class myClass:
    x=4          #class and static varible are same
    y=5


    @staticmethod
    def mySum():
        sum = myClass.x + myClass.y           #static method - direcrt acess from class
        print (sum)




myClass.mySum( )




obj =myClass()
obj.mySum()




print(obj.x)
print (myClass.y)       #same acess