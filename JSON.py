import json

#python to json string
"""
person ={             #obj
    "name":"nafi",
    "age":"23",
    "city":"sudbury",
    "title":["engineer","python"]
    
}

personJSON=json.dumps(person, indent=4)
print(personJSON)
"""



#JSONstring to  PYobject
"""
personJSON='{"name": "nafi", "age": "23", "city": "sudbury", "title": ["engineer", "python"]}'
perosnOBJ=json.loads(personJSON)
print(perosnOBJ['name']) 
"""


# python object     to   json string   to    file write
"""
person ={             #obj
    "name":"nafi",
    "age":"23",
    "city":"sudbury",
    "title":["engineer","python"]
}

with open("person.json","w") as personJSONFILE:
    json.dump(person,personJSONFILE,indent=4)
    print("done")
    """

# JSON file read   to    PY.obj    to    JSON string


with open("person.json","r") as personOBJFile:
    personOBJ= json.load(personOBJFile)
    print(personOBJ)
    personJSON = json.dumps(personOBJ, indent=4)
    print(personJSON)

