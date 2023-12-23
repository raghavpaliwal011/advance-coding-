try:
    i = int (input ("enter a number:"))
    c = 1/i
except Exception as e:
    print (e)
    exit()
finally:  # IMPORTANT note ----> spelling of this function should be finally not fianally
    print ("we are done")
