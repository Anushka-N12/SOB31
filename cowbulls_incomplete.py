import random

def compare_numbers(number1, user_guess,cowbullcount): #cowbullcount added as parameter
    ## your code here
    if user_guess in number1:
        if user_guess == number1[0]:#right place
            cowbullcount[1] = cowbullcount[1]+1
            number1 = number1[1:len(number)]
        else:
            cowbullcount[0] = cowbullcount[0]+1
    return cowbullcount, number1 #list renamed as per parameter, number1 added to return statement

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number) #brackets should be added
#above line shouldn't be printed in real life since its a game to guess it

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")
cowbullcount = [0,0] #index 0 counts cows and index 1 counts bulls
number1 = number #will edit this in function but need 'number' as it is to print after win
while playing:
    user_guess = input("Give me your best guess!") #raw_ removed since im using Python3
    if user_guess == "exit":
        break
    cowbullcount,number1 = compare_numbers(number1,user_guess,cowbullcount) #cowbullcount added here as argument and number changed to number1
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
    
    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")


