from abc import ABC , abstractmethod


class Ban(ABC):

    @abstractmethod
    def print10t020(self):
        pass


    @abstractmethod
    def print1t02(self):
        pass
    


    def print0to10(self):
        for i in range(10): 
         print(i+2)


class Dhaka(Ban):


   
   def print0to10(self):                     #override
      print("hello")


   def print10t020(self):                         #call abstract
      for i in range(5):
         print(i +1)


   def print1t02(self):
        print("print  1 10 2")                        #call abstact
    





obj=  Dhaka()
obj.print0to10()
obj.print10t020()
obj.print1t02()
