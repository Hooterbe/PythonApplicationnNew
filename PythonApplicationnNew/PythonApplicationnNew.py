#Shawn Merrigan
#Description - we have covered basic formatting and output data
#Numerical operators, variables, building expressions and inputting
#Data and converting the data.
#21 Sept 21
#Lab 2.1.1.18

print("hello Python!")
print('hello Python!')

print("Programming","Essentials","in")
print("Python")

#imput sep= and end= to add the *** and bring on one line us end=...

#Lab 2.1.1.19

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#Add the \n to add a space inbetween the tree to make it bigger
print("    *" , "\n")
print("   * *" , "\n")
print("  *   *" , "\n")
print(" *     *" , "\n")
print("***   ***" , "\n")
print("  *   *" , "\n")
print("  *   *" , "\n")
print("  *****" , "\n")
#The " needed to be spaced out and the *2 will double the tree so it is side by side
print("    *     " * 2, "\n")
print("   * *    " * 2, "\n")
print("  *   *   " * 2, "\n")
print(" *     *  " * 2, "\n")
print("***   *** " * 2, "\n")
print("  *   *   " * 2, "\n")
print("  *   *   " * 2, "\n")
print("  *****   " * 2, "\n")

#Lab 2.2.1.11

# "I'm"
# ""learning""
# """Python"""
print("\"I\'m\"" , "\n" , "\"\"learning\"\"" , "\n" , "\"\"\"Python\"\"\"" , sep="")

#Lab 2.4.1.7
#Add variables john = 3, mary = 5 and adam = 6
john = 3
mary = 5
adam = 6
#print all on the same line with a comma
print (john , mary , adam , sep=", ")
#add a variable called 'total_apples' and add total apples
total_apples = (john + mary + adam)
#print 'total_apples'
print(total_apples)

#Lab 2.4.1.9
#Workout miles to kilometers and vice versa
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Lab 2.4.1.10
#change the x = data with the input data to get different outcomes. 
#the equation needs to spread out so the computer can understand

x =  0
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x - 1)
print("y =", y)

x =  1
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x - 1)
print("y =", y)

x =  -1
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x - 1)
print("y =", y)

#Lab 2.5.1.2
#I have deleted any unused comments
#The vairable seconds was changed to b and the # removed from the second print line. 
#this program computes the number of seconds in a given number of hours
a = 2 # number of hours
b = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * b)
#this is the end of the program that computes the number of seconds in 2 hour

#Lab 2.6.1.9
#Change the comments into code. Add input a+b then add, subtract, multiply and divide.
#First was to change the input by adding a variable for a+b and the input code
#Next was to add print code for each line.
#print("\nThat's all, folks!")
a = float(input("Input your first number: "))
b = float(input("Input your second number: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("\nThat's all, folks!")

#Lab 2.6.1.10
#Write the code to work out 1/x+1/x+1/x+1/x
#Braces are used to breakdown the equation.

x = float(input("Enter value for x: "))

y = float(1/((x+1/(x+1/(x+1/x)))))

print("y =", y)

#Lab 2.6.1.11
#The code is working everything out in mins. The dura is in mins so mins + dura // 60.
#Hours and mins needed to be added together then divided by // 60 but floor division
#I then had to specify it was // 60 mins in 1 hour and answer %24 hrs.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura % 60
hour = hour + mins // 60 %24

print(hour, ":", mins, sep="")

