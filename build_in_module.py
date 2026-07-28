import math


print(math.sqrt(16))


import os

print(os.getcwd())


import sys

print(sys.version)


import datetime

CURRENT=   datetime.datetime.now()


print(CURRENT.hour)


import random

res = random.randint(1,6)

print(res)


import time

print(time.time())



import json

data = '{"name": "jhon"}'

jdata=json.loads(data)

print(jdata['name'])

