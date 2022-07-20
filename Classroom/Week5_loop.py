num_of_time = 0
while num_of_time <= 10:
    print("Hello World")
    num_of_time += 1 # mean when it is num_of_time is smaller than 5 it still print hello world

count = int(input("Number of cycle: "))
if count <= 0:
    print("Error")
elif count ==20: #only number 20 can exicute to OK
    print("ok")
else:
    x = 0
    while x < count:
        print("cycle")
        x +=1 # if we don't put it, it will loop forever
rows = int(input("Input Number:"))
#outer loop
for i in range(rows):
    #inner llop
    for j in range (i+1):
        print('*', end="") # end = delete space underline
    print(">>>>")

num = 0
for num in range (1,10):
    if num == 5:
        break
    elif num ==2:
        continue
    else:
        print (num)
    