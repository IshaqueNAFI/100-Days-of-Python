#creatre a zip file

"""

with open("new_zip","w")as file1:
    file1.write("hello IM creating a zip file")
    print("done")


"""
import zipfile

with zipfile.ZipFile("new.zip", "w") as zip:
    zip.write("demo_zip")



 
                                                          #un zip
                                                          
import zipfile

with zipfile.ZipFile('new.zip', 'r') as zip:
    zip.extractall()

                                      


