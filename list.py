fruits = ["apple","apple" ,"banana","cherry"]
fruits.append("mango")
fruits.remove("apple")
fruits.insert(1,"hello")


more_fruits = [ "egg ", "watermellon"  ]
fruits.extend( more_fruits)

lastItem=fruits.pop()
print(fruits)
print(lastItem)

"""
fruits.clear()
print(fruits )
"""

indexNO = fruits.index( "banana")
print(indexNO)


elementCount= fruits.count("banana")
print(elementCount)


fruits.sort()
fruits.reverse()

print(fruits)

lenght=len(fruits)
print(lenght)

print(fruits[1:4])


for eachFruit in fruits:
    print(eachFruit)
