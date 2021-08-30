import time  # import time for looks of program
import random  # import random for random number


# define the instruction section
def instructionsection():
    uplayed = input("Have you played my game before? ")  # ask if user has played to display instructions or not
    if uplayed == "n" or uplayed == "N" or uplayed == "no" or uplayed == "No" or uplayed == "nah" or uplayed == "Nah" or uplayed == "NO":  # ensure that what user answers is identified
        print("Well", name, ", let's hope you don't have beginner's luck.")
        time.sleep(2)  # improve look of program
        print("Alright,")
        print("I am thinking of a number between 1 and 100 and you can try to guess it.")
        time.sleep(4.5)  # improve look of program
        print("You will start with 10 score and every incorrect guess will decrease your score by 1.")
        time.sleep(5)  # improve look of program
        print("Every correct guess will add 1 to your score.")
        time.sleep(3)  # improve look of program
        print("I will count the number of guesses you take, the higher the better.")
        time.sleep(3)  # improve look of program
        print("The game will end when your score reaches 0.")
        time.sleep(3)  # improve look of program
        print("So don't be too random.")
        time.sleep(2)  # improve look of program
        print("Can you guess it?")
        time.sleep(1)  # improve look of program
        print("Your score is 10")
        time.sleep(1)  # improve look of program
    elif uplayed == "y" or uplayed == "Y" or uplayed == "yea" or uplayed == "Yea" or uplayed == "yes" or uplayed == "Yes" or uplayed == "yep" or uplayed == "Yep":  # ensure that what user answers is identified
        print("Welcome back then.")
        time.sleep(1)  # improve look of program
        print("Lets see if you can beat my creator's best score, which is 16 guesses.")
        time.sleep(2.5)  # improve look of program
        print("Alright, I have my number.")
        time.sleep(1)  # improve look of program
        print("Your score is 10")
        time.sleep(1)  # improve look of program
    else:  # ensure that users enters allowed character/s
        print("You didn't input an allowed answer.")
        print("Try 'y' for yes and 'n' for no.")
        instructionsection()  # call function to repeat
    return


def firstgameover():  # define the game over function
    print("Oh No!")
    time.sleep(1)  # improve look of progam
    print("Your score is now 0.")
    time.sleep(1)  # improve look of progam
    print("You were close but the number you were looking for was", number1)  # inform user of the required number
    time.sleep(2)  # improve look of progam
    print("I'm so sorry", name, ", I thought you would get it.")
    time.sleep(2)  # improve look of progam
    print("But this means your game is...")
    time.sleep(1.5)  # improve look of progam
    print("")  # graphics to show game over
    print("   ________      ___           ___     _________       _________")
    time.sleep(0.4)  # improve look of progam
    print(" /   ____   \    \  \         /  /    |   ______|    /   _______|")
    time.sleep(0.4)  # improve look of progam
    print("|  /      \  |    \  \       /  /     |  |______     |  |")
    time.sleep(0.4)  # improve look of progam
    print("| |        | |     \  \     /  /      |  |______|    |  |")
    time.sleep(0.4)  # improve look of progam
    print("|  \ ____ /  |      \  \___/  /       |  |______     |  |")
    time.sleep(0.4)  # improve look of progam
    print(" \ ________ /        \_______/        |_________|    |__|")
    print("")  # improve look of progam
    print("")  # improve look of progam
    time.sleep(3)  # improve look of program
    print("But you did last", guesses, "guesses.")  # display users number of guesses
    time.sleep(1.5)  # improve look of program
    print("Better luck next time!")
    time.sleep(1)  # improve look of program
    exit()  # exit program


def gameover():  # define the game over function
    print("Oh No!")
    time.sleep(1)  # improve look of program
    print("Your score is now 0.")
    time.sleep(1)  # improve look of program
    print("You were close but the number you were looking for was", number)  # inform user of the required number
    time.sleep(2)  # improve look of program
    print("I'm so sorry", name, ", I thought you would get it.")
    time.sleep(2)  # improve look of program
    print("But this means your game is...")
    time.sleep(1.5)  # improve look of program
    print("")  # graphics to show game over
    print("   ________      ___           ___     _________       _________")
    time.sleep(0.4)  # improve look of program
    print(" /   ____   \    \  \         /  /    |   ______|    /   _______|")
    time.sleep(0.4)  # improve look of program
    print("|  /      \  |    \  \       /  /     |  |______     |  |")
    time.sleep(0.4)  # improve look of program
    print("| |        | |     \  \     /  /      |  |______|    |  |")
    time.sleep(0.4)  # improve look of program
    print("|  \ ____ /  |      \  \___/  /       |  |______     |  |")
    time.sleep(0.4)  # improve look of program
    print(" \ ________ /        \_______/        |_________|    |__|")
    print("")  # improve look of program
    print("")  # improve look of program
    time.sleep(3)  # improve look of program
    print("But you did last", guesses, "guesses.")  # display users number of guesses
    time.sleep(1.5)  # improve look of program
    print("Better luck next time!")
    time.sleep(1)  # improve look of program
    exit()  # exit program


def guesschecker(guess):
    while True:
        '''if not guess.isdigit():
            print("Oops, you did not enter a digit between 1 and 100.")
            time.sleep(1)
            print("Please try again.")
            print("")
            continue
        guess = int(guess)
        if guess <= 0 or guess >= 101:
            print("Oops, you did not enter a digit between 1 and 100.")
            time.sleep(1)
            print("Please try again.")
            print("")
            continue
        else:
            break'''
        try:
            guess = int(input("enter guess"))
        except (ValueError):
            print(("incorrect entry, Retry"))
            continue
        else:
            break


    return int(guess)


def guess1checker(guess1):

    while True:
        try:
            guess = int(input("enter guess"))
        except (ValueError):
            print(("incorrect entry, Retry"))
            continue
        else:
            break
        '''
        if not guess1.isdigit():
            print("Oops, you did not enter a digit between 1 and 100.")
            time.sleep(1)
            print("Please try again.")
            print("")
            continue
        guess1 = int(guess1)
        if guess1 <= 0 or guess1 >= 101:
            print("Oops, you did not enter a digit between 1 and 100.")
            time.sleep(1)
            print("Please try again.")
            print("")
            continue
        else:
            break'''
    return guess1


def lastguesschecker(guess):
    while True:
        try:
            guess = int(input("enter guess"))
        except (ValueError):
            print(("incorrect entry, Retry"))
            continue
        else:
            break

        if guess <= 0 or guess >= 101:
            print("Oops, you did not enter a digit between 1 and 100.")
            time.sleep(1)
            print("Please try again.")
            print("")
            continue
        else:
            break
    return guess

#start
print("Hello User! To start, I will need your name.")  # greet user and ask their name
time.sleep(1)  # improve look of progam
name = input("Please enter your name here: ")  # give 'name' a variable
print("Well", name, ", Let's play a game.")
time.sleep(2)  # improve look of progam

instructionsection()  # execute the instructionsection def

counter = 10  # set score
guesses = 0  # set number of guesses

number1 = random.randint(1, 100)  # generate random number
guess1 = input("Give it a go: ") # ask first guess
x=guess1checker(guess1)
guess1 = x

guesses = guesses + 1  # add a guess to the guess counter
print("")  # improve look of program
if guess1 == number1:  # skip the wrong answer section is user entered correct number
    print("On the first try!")
    print("That's quite impressive")
    guesses = guesses + 1  # add a guess to the guess counter
while guess1 != number1:  # loop until the answer is right or they have lost
    if counter == 2:  # query to if last guess loop can be played
        if guess1 < number1:  # check if too high or too low
            print("That's not it!")
            print("Your guess was too low.")
            counter = counter - 1  # edit score value appropriately
            guesses = guesses + 1  # add a guess to the guess counter
            print("Your score is now ", counter)  # display user's score
            lastguess = input("Try again: ")  # receive input for last guess
            print("")  # improve look of program
            lastguessret =lastguesschecker(lastguess)
            if lastguessret != number1:  # play if user was incorrect
                firstgameover()  # call the game end function
            if lastguessret == number1:  # play if user was correct
                break  # exit while loop
        elif guess1 > number1:  # check if too high or too low
            print("That's not it!")
            print("Your guess was too high.")
            counter = counter - 1  # edit score value appropriately
            guesses = guesses + 1  # add a guess the guess counter
            print("Your score is now ", counter)  # display user's score
            lastguess = input("Try again: ")  # receive input for last guess
            print("")  # improve look of progam
            lastguessret = lastguesschecker(guess1)
            if lastguessret != number1:  # play if user was incorrect
                firstgameover()  # call the game end function
            if lastguessret == number1:  # play if user was correct
                break  # exit while loop
    else:
        if guess1 < number1:  # check if too high or too low
            print("That's not it!")
            print("Your guess was too low.")
            counter = counter - 1  # edit score value appropriately
            guesses = guesses + 1  # add a guess the guess counter
            print("Your score is now ", counter)  # display user's score
            guess1 = input("Try again: ")  # receive user's updated guess
            print("")  # improve look of program
            guess1checker(guess1)
        elif guess1 > number1:  # check if too high or too low
            print("That's not it!")
            print("Your guess was too high.")
            counter = counter - 1  # edit score value appropriately
            guesses = guesses + 1  # add a guess the guess counter
            print("Your score is now ", counter)  # display user's score
            guess1 = input("Try again: ")  # receive user's updated guess
            print("")  # improve look of program
            guess1checker(guess1)

if guess1 == number1 or lastguess == number1:  # play correct answer section and move on to looping section
    print("Well done, you guessed my number!")
    counter = counter + 1  # edit score value appropriately
    guesses = guesses + 1  # add a guess the guess counter
    print("Your score is now ", counter)  # display user's score
    time.sleep(2)  # improve look of program

while counter != 0:  # keep asking user for guesses and continue their game until they lose
    print("Your doing well, let's continue.")
    time.sleep(2)  # improve look of program
    print("I'm going to think of a new number that you'll never get.")
    time.sleep(4)  # improve look of program
    print("Ok, I've got a new number")
    time.sleep(1)  # improve look of program
    number = random.randint(1, 100)  # generate new random number
    guess = input("Let's go again: ")  # ask for the new number.
    guesschecker()
    print("")  # improve look of program
    while guess != number:  # play the wrong answer section
        if counter == 2:  # query to if last guess loop can be played
            if guess < number:  # check if too high or too low
                print("That's not it!")
                print("Your guess was too low.")
                counter = counter - 1  # edit score value appropriately
                guesses = guesses + 1  # add a guess to the guess counter
                print("Your score is now ", counter)  # display user's score
                lastguessloop = int(input("Try again: "))  # ask user's last guess
                print("")  # improve look of program
                lastguessloop = lastguesschecker()
                if lastguessloop != number:  # play if user was incorrect
                    gameover()  # call the game end function
                if lastguessloop == number:  # play if user was correct
                    break
            elif guess > number:  # check if too high or too low
                print("That's not it!")
                print("Your guess was too high.")
                counter = counter - 1  # edit score value appropriately
                guesses = guesses + 1  # add a guess the guess counter
                print("Your score is now ", counter)  # display user's score
                lastguessloop = input("Try again: ")  # receive input for last guess
                print("")  # improve look of program
                lastguessnum = lastguesschecker()
                if lastguessloop != number:  # play if user was incorrect
                    gameover()  # call the game end function
                if lastguessloop == number:  # play if user was correct
                    break  # exit while loop
        else:
            if guess < number:  # check if too high or too low
                print("That's not it!")
                print("Your guess was too low.")
                counter = counter - 1  # edit score value appropriately
                guesses = guesses + 1  # add a guess the guess counter
                print("Your score is now ", counter)  # display user's score
                guess = input("Try again: ")  # receive user's updated guess
                print("")  # improve look of program
                guesschecker()
            elif guess > number:  # check if too high or too low
                print("That's not it!")
                print("Your guess was too high.")
                counter = counter - 1  # edit score value appropriately
                guesses = guesses + 1  # add a guess the guess counter
                print("Your score is now ", counter)  # display user's score
                guess = input("Try again: ")  # receive user's updated guess
                print("")  # improve look of program
                guesschecker()
    if guess == number:  # play if user was correct
        print("Well done, you guessed my number!")
        counter = counter + 1  # edit score value appropriately
        guesses = guesses + 1  # add a guess the guess counter
        print("Your score is now ", counter)  # display user's score
        print("")  # improve look of program
