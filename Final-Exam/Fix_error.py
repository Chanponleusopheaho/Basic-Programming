Height = float(input("Enter your height in centimeters: "))
Weight = int(input("Enter your Weight in kg:"))
Height = Height/100 #Covert centimeter to meter
BMI= Weight / Height ** 2
print("Your Body Mass Index is: ", BMI)
if(BMI < 0):
    print("Enter valid detail.")
if(BMI <= 16):
    print("You are severely underweight.")
elif(BMI <= 18.5):
    print("You are underweight.")
elif(BMI <= 25):
    print("You are Healthy.")
elif(BMI <= 30):
    print("You are overweight.")
else:
    print("You are severely overweight.")