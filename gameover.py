import time

def gameover(name, number,guesses):  # define the game over function
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
    return

name=input("enter name")
number=int(input("enter your guess"))
guesses = 0
gameover(name,number,guesses)
