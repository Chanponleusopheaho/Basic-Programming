def binary(decimal):
    bi=0
    m=1
    while decimal>0:
        bi = bi+((decimal%2)*m)
        m = m*10
        decimal=int(decimal/2)
    return bi
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
def Hex(num): 
    hexadecimal = ''
    while(num > 0):
        remainder = num % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        num = num // 16
  
    return hexadecimal
for num in range(1,16,1):
    print(num, binary(num),  Hex(num))