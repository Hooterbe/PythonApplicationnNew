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

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)