number = 0
while number <= 99:
    number +=1
    for a in range(2,number): 
        if number % a == 0:
            print (number, " is not a prime number")
    else: 
        print ( number," is a prime number")
