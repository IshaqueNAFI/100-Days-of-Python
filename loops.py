"""list1= ["apple","mango","banana", "cherry", "date", "elderberry"]
print(list1[0])
print(list1[1])
print(list1[2])
print("      ")




fruits= ["grape","kiwi","lemon", "melon", "nectarine", "orange"]
value = int(input("enter a number: "))

if (value >= 5) :

  for eachitem in fruits:
    print(eachitem)

else :
    word= "banana"
    for eachletter in word:
        print   (eachletter)
       


for item in range(4):
    print(item)


marks = {
'phy':90 , 
'chem':85,
'math':92
}
for subject, marks in marks.items():

    print (subject)
    print (marks)
    print ("{}:{}".format(subject,marks))

    print( "sub:" + subject + "   marks:" + str(marks))


unique_numbers= {1,3,4,5,5,6,6,7}
for eachNumber in unique_numbers:
 print (eachNumber)


 """

for num in range (10):
    if num ==5:
        continue
    print(num)

for num in range (10):
    if num ==5:
        break
    print(num)

