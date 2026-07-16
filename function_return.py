"""def addTwo (a,b):
    
    num1=a
    num2=b
    sum=num1+num2
    sub=num1-num2
    div = num1/num2
                         #return[sum, sub,div]
    return{"sum":sum,"sub":sub, "div":div}

result=addTwo(3,4)
print(result)

"""

def num(numbers):
    for number in numbers:
        if number%2==0:
            return number
        


    return None
    


   
   
   
result=num([1,2,3,5,3,8,2,2,4])
print(result)