#This a tip calculator

print("Welcome to the tip calculator")
amount_of_the_bill = input("What the total bill? $")
tip_amount = input("How much tip would you likr yo give? 10, 12 or 15? ")
amount_of_people = input("How many people to split the bill?")

each_person_amount = round((float(amount_of_the_bill )/ int(amount_of_people))*(1+(int(tip_amount)/100)), 2)

print(f"Each Person should pay {each_person_amount}")