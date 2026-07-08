"""number=range(1, 22)
print(*number)
print("Done!")
num2=range(1, 22,2)
print(*num2)
num3=range(5)
print(*num3)   
isBD=False
print(isBD)
taka=None
print(taka)

person={
    'name' : 'nafi',
    'age' : 22,
    'isBD' : False,
    'taka' : None }     

print(person['name'])


unique_num={1, 2, 3, 4, 5, 6, 7, 8, 9,1,2} 
print(list(unique_num)) 

unique_num=frozenset([1, 2, 3, 4, 5, 6, 7, 8, 9,1,2]) 
print(unique_num)




a=1
b=2.3444       #immutable data type
c=True
d=None
e="nafi"
p ={
    'name' : 'nafi',
    'age' : 22,
    'isBD' : False,
    'taka' : None }     
s={1,23,4,2.1}
print(type(a))
print(type(b))
print(type(p))
print(type(s))
check=type(c)
print(check)

a=(1,2,3,4,5)
initial_value=id(a)
a=(1,2,3,4)
second_value=id(a)
print(initial_value)
print(second_value)

l= [1,2,3,4,5  ]          #mutable data type
first_value=id(l)
print(first_value)
l[0]= 9
second_value=id(l)
print(second_value)
print(l)


d= {'a': 2, 'b': 4}
first_value=id(d)
print(first_value)
d['a']= 9
second_value=id(d)
print(second_value)
print(d)

s={1,2,3,4,5}
first_value=id(s)
print(first_value)
print(s)
s.add(9)
second_value=id(s)
print(second_value)
print(s)


x= "13"           #explixit type conversion
y = int(x)
z=float(x)
print(y)
print(z)

x=10              #implicit type conversion
y=12.2
z=x+y
print(z)
"""

try:
    a="nafi"
    b=int(a)
    print(b)

except Exception as e:
    print(e)
    