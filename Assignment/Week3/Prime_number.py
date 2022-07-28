number = 0
number in range (1,101)
while number <= 99:
    for a in range(2,number): 
        if number % a == 0:
            print (number, " is not a prime number")
else: 
    print ( number," is a prime number")
    number +=1