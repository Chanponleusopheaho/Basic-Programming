num =[]
Odd_num = []
Even_num = []
for x in range (0, 101): 
    num.append(x)
    if x % 2 == 0:
        Even_num.append(num[x])
    else:
        Odd_num.append(num[x])
print("Even numbers List:",Even_num)
print("Odd numbers List:", Odd_num)