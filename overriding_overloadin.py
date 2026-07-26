class Father:
    x=4
    y=5

    def add(self):
        print(self.x+self.y)



class son (Father):
    def add (self):
        print(self.x +self.y+100)


obj = Father()
obj.add()

obj1= son()
obj1.add()



