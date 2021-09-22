#Shawn Merrigan mod 3
#Lab 3.1.1.4
#Enter an input code for any number then
#add n greater or equals to. If below 100 it's false

n = int(input("enter a number : "))

print (n > 100)

#Lab 3.1.1.10
#An input was needed then responses to the correct and incorrect asnwers.
#If, elif and else were used. : is needs after the if, elif and else command

flower = input("Input a flower name:")

if flower == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
    
elif flower == "spathiphyllum":
    print ("No, I want a big Spathiphyllum!")
    
else: 
    print ("Spathiphyllum! Not", flower + "!")

#Lab 3.1.1.11
#This section uses if,, else.
#If income < 85528, income is x 18% and - 556.02 = tax
#If income is > 85528, minus income with 85528, x surplus by 32%
#Add 14839.02 = tax
#If tax <= 0, no tax is paid.

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02
    
if tax <= 0:
    tax = 0
  
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#Lab 3.1.1.12
#If year is less than 1582 print("not") text
#If year is not divisable by 4 or 400 print ("common year")
#If year is not divisable by 100 or anything else print("Leap year")

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
    
else:
    if (year % 4) + (year % 400) != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    else:
        print("Leap year")

