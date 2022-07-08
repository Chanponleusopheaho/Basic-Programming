number = 1
while number <= 100:
    number +=1
    for a in range(1,number): 
        if (number % a) == 0:
            print (number, " is not a prime number")
    else: 
        print ( number," is a prime number")
