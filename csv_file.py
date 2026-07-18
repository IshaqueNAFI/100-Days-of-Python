"""import csv               #creating a csv file

data =  [

["name","nafi",798888]


]

with open ("new.csv","w") as file:
    csv_file= csv.writer(file)
    csv_file.writerows(data)
    print("done")

    """


                                 # reading a csv file

import csv
with open("new.csv","r") as file:
   content= csv.reader(file)
   for files in content:
        print(files)