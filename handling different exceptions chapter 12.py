try:
    a = int (input("enter a number : "))
    c = 1/a
    print (c)
except ValueError as e:
    print ("please enter a valid value")

except ZeroDivisionError as e:
    print ("make sure you are not dividing by 0")

print ("thanks for using this code! ")