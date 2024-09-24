#This program determinates if a year enter by the user is a leap year. 

year = int(input("Enter a year "))

if year % 400 == 0 & year % 100 == 0:
    print(f"{year} is a leap year.")
elif year % 4 == 0 & year % 100 != 0:
    print(f"{year} is a leap year.")
else:
       print(f"{year} isn't a leap year.")