class Car:

    __model= "toyota"

    @property

                            #to get the value use @property and use return
    def BRAND(self):
        return self.__model

    

    @BRAND.setter                   #to set the value use the @name.setter and use a variable parameter
    def newBRAND(self, value):
        self.__model = value



obj=Car()
obj.newBRAND = "MAJDA "     #set

#get
print(obj.BRAND)

