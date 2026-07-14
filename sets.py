fruits= {"apple" ,"apple", "banana","cherry" }
print(fruits)
print(id(fruits))
fruits.add("mango")

print(id(fruits))
fruits.remove("banana")
print(fruits)


fruits.update(["garpe"])

print(fruits)
fruits.clear()

print(fruits)


set1={1,2,4,4,9}
set2={4,5,7}

result= set1.union(set2)

print(result)


result2= set1.intersection(set2)
print(result2)



result3= set1.difference(set2)
print(result3)