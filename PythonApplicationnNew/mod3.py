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

#Lab 3.2.1.3
#If the number is not equal to secret_number run loop.
#If it is, print number and the muggle is free.
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

#will ask the user to enter an integer number;
number = int(input("Enter a integer number: "))
print(number)

#will check whether the number entered by the user is the same 
#as the number picked by the magician. If the number chosen by the 
#user is different than the magician's secret number, 
#the user should see the message 
#"Ha ha! You're stuck in my loop!"

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    #prompted to enter a number again. 
    int(input("Enter a integer number: "))
    

else:
        print("Well done, muggle! You are free now.")

#Lab 3.2.1.6
#Use the 'for' loop and range 1 - 6 to count and print 1 mississippi - 5 mississippi
#Using 'else' the end message should read 'Ready or not, here I come!'
import time

# Write a for loop that counts to five.
for t in range (1, 6):
    # Body of the loop - print the loop iteration number and 
    #the word "Mississippi".
    print(t, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
else:
    # Write a print function with the final message.
    print("Ready or not, here I come!")

#Lab 3.2.1.9 
#Setup a loop for a user to enter a word, if its not the correct word
#The loop continues. If correct, a message appears and the loop breaks.

while True:
    word = (input("Enter a word: "))
    if word == ("chupacabra"):
        print("You've successfully left the loop.")
        break

#Lab 3.2.1.10
#Create a for loop that will show letters that are not vowels.
user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

#Lab 3.2.1.11
#Print the remaining words as a string but adding a variable
#and += letter
word_without_vowels = ""

user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
		
print(word_without_vowels)

#Lab 3.2.1.14
#I copied this in
blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)

#Lab 3.2.1.15
#I copied again. This is not the answer but I will do some
#YouTube work so it falls into my head. 
c0 = int(input("Enter a positive number - c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")