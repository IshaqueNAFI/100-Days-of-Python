class car:

    __brand="toyota"
    def display(self):
        print("our brand name is " +self.__brand)              #inside class call




class sedan(car):
    def displayChild(self):
         print(f"our brand anme is {self.__brand}")  

        

 
obj = sedan()
obj.display()    

# print(obj.__brand)
#obj.displayChild()
#print(obj.__brand)  #outside variable call
