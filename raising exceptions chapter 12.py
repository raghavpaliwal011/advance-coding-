def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not good = raghav") 
    
a = increment (364)
print (a)