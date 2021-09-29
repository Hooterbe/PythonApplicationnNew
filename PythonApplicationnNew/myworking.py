#This is just my notes on how to do different things
#This is how to work out time or durations

#The code is working everything out in mins. The dura is in mins so mins + dura was needed.
#Hours and mins needed to be added together then divided by // 60 but floor division
#The mins had to work out it has to be less than 60 and the hours less than 24.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

days = int(input("number of days (days): "))
weeks = int(input("number of weeks (weeks): "))
dura = int(input("number of days (days): "))

days = days + dura
weeks = weeks + days // 7
days = days % 7
weeks = weeks % 52
print(weeks, "weeks" ",", days, "days" ".", sep="")

#This is how to ask for information i.e names

fname = input("Enter your name: ")
lname = input("Enter your name: ")
print("Hello, " + fname + " " + lname + ". Nice to meet you!")

#If you wanted to repeat something x amount of times
x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")

var == 0

#How to create an input

a = int(input("enter number : "))

#How to use the if else code

# long version
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# short version
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# If more than two numbers

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# Using the max/min function
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

# if, elif and else using words

flower = input("Input a flower name:")

if flower == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
    
elif flower == "spathiphyllum":
    print ("No, I want a big Spathiphyllum!")
    
else: 
    print ("Spathiphyllum! Not", flower + "!")

    #Workin out tax or number values
    income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02
    
if tax <= 0:
    tax = 0
  
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#Working out how to create code for leap years. 
#Remember to add : and the end of the if, elif, else function.

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

# Loops
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


#Loops counting down
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#Break and continue
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

########### Lists 
#Listing numbers and changing certain parts.
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content with the first numnber as 111.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers) 

################ sorting lists and numbers

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

############# Easy sort

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

my_list.sort()
print(my_list)

####### working out BMI

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(100, 1.65))

def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(184.9))

def kg_to_lb(kg):
    return kg * 2.2


print(kg_to_lb(84))

######### Finonacci numbers

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 99):  # testing
    print(n, "->", fib(n))
