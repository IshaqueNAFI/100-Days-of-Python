import datetime

current=datetime.datetime.now()
formated_datetime= current.strftime("%d/%m/%Y   %H:%M:%S"  )
print(formated_datetime)


"""
print(current)
print(current.month)
print(current.time)
print(current.second)
"""


                                          #time differee


date1= datetime.datetime(2026,7,21)
date2= datetime.datetime(2024,8,10)

dif = date1-date2
print(dif)


new_date=date1+datetime.timedelta(days=12)
print(new_date)
