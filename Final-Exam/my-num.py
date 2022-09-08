file_object = open("C:/Users/Chanponleusophea Ho/OneDrive/Documents/CamTech University/Year 1/Term 1/Basic Programming/Python/Final-Exam/my_num.txt")
#if file_object:
    #print("Ok")
#num_list = (float(num) for num in file_object.read().split())
my_num = file_object.read()
num_list = my_num.split()
#res = [eval(i) for i in num_list]
print("All my number:",my_num)
print("The lowest number is:",min(num_list))
print("The largest number is:",max(num_list))


min_num_int = int(min(num_list))
max_num_int = int(max(num_list))
print("The summation between the lowest and the largest numbers is:",(min_num_int+max_num_int))