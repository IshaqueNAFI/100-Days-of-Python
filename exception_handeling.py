#10/0
#file not found
#try and except and
"""
try:
    result=10/0
    print(result)

except ZeroDivisionError:
    print("division by 0")


"""
try:
    with open("new.error",'r' ) as file:

        content=file.read()
        result=10/int(content)
        print(result)



except Exception as e:
    print(e)

"""  
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("value error")
except TypeError:
    print("typing error")
except ZeroDivisionError:
    print("division by 0")

"""
try:
    result =10/0
    print(result)
except Exception as e:
    print (e)

finally:
    print("execution completed")

    






