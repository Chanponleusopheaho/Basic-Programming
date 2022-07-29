birth_date = int(input("Which date you were born? (Please enter in number, Ex. 26): "))
if birth_date > 31:
    print("Error")
elif birth_date <0: 
    print("Error")
birth_month = int(input("Which month you were born? (Please enter in number, Ex. 5): "))
if birth_month >12:
    print("Error")
elif birth_date <0: 
    print("Error")
birth_year = int(input("Which year you were born?(Please enter in number, Ex. 2005):"))
if birth_year >2022:
    print("Error")
days_in_year = 365
date_today = 29
calculate_year = 2022 - birth_year

age = int((date_today - birth_date)/ days_in_year) + calculate_year
print("Your age is: ",age) 