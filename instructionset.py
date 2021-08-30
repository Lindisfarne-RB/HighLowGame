import time
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

instructionsection()