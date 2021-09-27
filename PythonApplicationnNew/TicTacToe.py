#using lists within lists, create a means of storage for a TTT tic tac toe game, noughts and crosses
#the TTT board is 3 rows and 3 columns
#Before continuing, read the below code which shows how to create a chess board
#https://github.com/chrishoran8/PythonEssentialsModule3/blob/master/PythonEssentialsModule3/rowsSection.py
#As you can see, there are multiple ways to do this. The only requirement is that you get it working
#However, if you want to challenge yourself, get it working in as little lines of code as possible

# Step 1: Create the board
tttBoard = [["_" for c in range(3)] for r in range(3)]

# Step 2: Output the board to the screen
print ("Current Board: ")        

print (tttBoard[0])
print (tttBoard[1])
print (tttBoard[2])

# While loop will allow multiple entries onto the board.
while True:

# This for loop is prompting the user to input the column value
    for column_input in tttBoard:
        column_input = int(input("Select Column: "))
        if column_input <= 3: # Conditional checking. If the value is over 3, the loop will reset until a valid value is input.
            break # If the value of column_input is 3 or below it will break out of the loop.
        else:
            print ("Invalid Entry!!") # If the user does not input an appropriate number it will display the following error message.

# Similar to the above loop, but for the row input
    for row_input in tttBoard:
        row_input = int(input("Select Row: "))
        if row_input <= 3: # Conditional checking. If the value is over 3, the loop will reset until a valid value is input.
            break # If the value of column_input is 3 or below it will break out of the loop.
        else:
            print ("Invalid Entry!!")

# This for loop is asking whether the user wants to put a nought or a cross on the board.
    for Selection in tttBoard: # Asking the user to input whether they are choosing a nought or a cross.
        Selection = str(input("Selection: o or x?: "))
        if (Selection == 'o') or (Selection == 'x'): # If a valid nought or cross, it will be set to the value in the list.
            tttBoard[row_input-1][column_input-1] = Selection # As the index values begin at 0, the input for column and row will need to be reduced by 0 to fit in the list.
            break
        else:
            print ("Invalid Entry!!") # # If the user input is not a nought or a cross, the following error message will display.
    # Part of the while loop. Will display the board after every entry.
    print ("Current Board: ")        
   
    print (tttBoard[0])
    print (tttBoard[1])
    print (tttBoard[2])