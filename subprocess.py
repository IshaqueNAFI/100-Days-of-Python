"""import subprocess

result = subprocess.run(

    ['python' ,'--version'],
capture_output=True,
text=True
)

print(result.stdout)

                                #hash 
import hashlib

password= b"ABC12"

has_object= hashlib.sha256(password)

print (has_object.hexdigest())

"""

import csv

with open ('data.csv', 'w') as file:

    writer = csv.writer(file)

    writer.writerow(['name' , ' nafi'])

