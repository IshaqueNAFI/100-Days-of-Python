def say_hello( ):

    print("hello world")
 

say_hello()

def dic(**names):
    print(names)

def tuples(*numbers):
    for number in numbers:

       print(number)

def addTwo(a=0,b=0):  #default parameter



    num1= a
    num2 = b

    print(num1+num2)



addTwo(12,3)
addTwo(2,3)
addTwo(9,4)
addTwo(7)

tuples(2,3,4,5,6,6)
