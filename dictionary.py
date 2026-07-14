person={
    "name": "nafi",
    "name": "pafi",
    "age" : 23,
    "city": "sudbury"

}
print(person["age"])
print(person.get("age"))
print(id(person))
print(person)

person.update({"name":"israil"})   
print(id(person))
print(person  )

print(person.keys())

print(person.values( ))

print(person.items())

x=person.pop("age")
print(person)
print(x)
