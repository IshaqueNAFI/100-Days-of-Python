#create and write
with open("example.text","w") as file:
    print("created")
    file.write("hello python")
    

#read
with open("example.text","r") as file:
    content= file.read()
    print(content)


#rename
"""
import os 
os.rename("example2.text", "example3.text")
"""

#remove
import os
os.remove("example3.text")




  

