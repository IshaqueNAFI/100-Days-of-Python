#local variable

def result2(x,y):
    num1=x
    num2=y

    sum=num1+num2
    print(sum)

result2(4,5)


#globall variable


n=5
m=1

def result2(a,b):
   
    sub=n-m
    print(sub)


result2(6,2)

print(n+m)


text="hello global"

def myFun():
    text="hello local"
    print(text)


myFun()

print(text)



x=10

def sum1():
    global x
    x=6
    result=x+1
    print(result)

sum1()

def sum2():
    result=x+2
    print(result)

sum2()
