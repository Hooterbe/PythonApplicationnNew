##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Shawn Merrigan
##Course Number: 1/20
##Student Number: N/A


#####################################################
#Section 1 25 Marks


#1) Create and Assign a type float variable called fltOne the value 10 (3)

fltOne = 10.0 #Created the variable called fltOne and assisgn float number 10.0
print(fltOne)

#2) Create and Assign a type float variable called fltTwo the value 20 (3)

fltTwo = 20.0
print(fltTwo)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)

fltThree = fltOne, fltTwo #Added both of the variables to fltThree
print(fltThree)

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)

stringOne = ("The product of fltOne and fltTwo = ")
print(stringOne)

#5) On the console, output stringOne and fltThree (in that order) (3)

print(stringOne, fltThree)

#6) increment fltOne  (3)

fltOne = fltOne + 1 #Adds 1 to the variable fltOne
print(fltOne)

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)

a = float(input("Please provide another number for fltTwo: ")) #This is a variable for the input
fltTwo = fltTwo + a # puts both variables on the same line as an output
print(fltTwo)

#8) on the console, output the product of fltOne and flotTwo with a suitable message (3)

print("The output for fltOne and fltTwo is:",fltOne, fltTwo, sep= " ") #Output of fltOne and fltTwo

#####################################################
#Section 2 35 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted .
#The decision should be based on if the user inputs a number below 100
#the code should output "below 100" (5)

if a < 100: #Argument for it the input is less than 100
    print("below 100")

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
#Using if, else and elif, output the following:
#If the product is below 0, output "below 0"
#if the product is 0 output "value is zero"
#if the product is above 0 output "above 0" (8)

g = (fltOne - fltTwo)

if g < 0:
    print("below o")
if g == 0:
    print("value is zero")
if g > 0:
    print("above 0")



#10) create a list called listOfInts (4)

listOfints = []

#11 part a) create a for loop to iterate through the above list and populate the list with
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)

listOfints = [2 * x for x in range(12)[2:]]

print(listOfints)

#11 part b) create a for loop to iterate through the above list and
#multiply each value by three assigning the new value to the respective
#index in the list. The list should now look like {12,18,24.....} (8)

total = [i * 3 for i in listOfints]
listOfints = total
print(listOfints)

#11 part c )output listOfInts to the screen with a suitable message (3)

print("The output for listOfints is: ", listOfints)

#####################################################
#Section 3 20 marks

#14) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost less the percentage amount
#For example if the paramenters are cost = 100 and percentage = 50, it should return 50.
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
#The percentage value should assume 10% if no value is given
#print a test to the screen with cost set as 50 and percentage set as 10

def calcPerc():
    n = input("Do you want a custom percentage 'yes' or 'no': ")
    if n == "yes":
        money = int(input("Enter a your start money: "))
        perc = int(input("Enter the percentage: "))
        totalperc = int(money / 100 * perc)
        minusperc = (money - totalperc)
        print(minusperc)

    else:
        money = int(input("Enter a your start money: "))
        perc = 10
        totalperc = int(money / 100 * perc)
        minusperc = (money - totalperc)
        print(minusperc)

calcPerc()

#15) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.

def caseChanger():
    user_word = input("Enter your word: ")
    user_word = user_word.lower()
    for letter in user_word:
        if letter == 'e':
            print(letter.upper(), sep="", end="")
        if letter != 'e':
            print(letter, sep="", end="")

caseChanger()
print("")

#####################################################
#Section 4 20 marks

#16)a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)

students = ["Clark", "Horan", "Rai", "White", "Cooper", "Jones", "Cox", "Smith"]
print(students)

#b) use a method to order the students so that they are in alphabetical order (3 marks)

students.sort()
print(students)

#17) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93

Exam_Marks = (65,66,67,80,90,65,65,93)
print(Exam_Marks)

#18) Dictionary question (9 marks)
#create a dictionary
#write code which adds both the student and a their corresponding mark.
#do not perform this long hand (as in writing out the values above). Use data
#from the existing tuples above to create the dictionary

dictionary = {}
print(dictionary)

students_tuple = tuple(students)

dictionary = tuple(zip(students_tuple, Exam_Marks))
print(dictionary)
