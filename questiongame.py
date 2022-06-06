#------------------------Question Game-------------------------------------------
#Be able to clear the screen to remove any extra texts
import os

#Title
os.system('cls')
play = input("Quiz Game! Would you like to play?(Yes to begin.)\n")

if (play.upper() != "YES"):
    quit()
else:
    #Actual game starts
    os.system('cls')
    username = input("Hello challenger! Before we begin, may I ask what is your username?\n")

    #Rules section
    os.system('cls')
    knowthegame = input("Welcome "+username+", do you know how this game is played?\n(Y for Yes or type anything else for No)")
    os.system('cls')
    if(knowthegame.upper() != "Y"):
        knowthegame = input("It's a simple game that challanges the player with a question but don't worry we will provide 4 possible answers.\nThe only thing we need from you is to spot the correct answer by typing the number associated with it.\nDo you understand? (Y for Yes or type anything else for No)")
        os.system('cls')
        if (knowthegame.upper() != "Y"):
            input('Here is an example: \nWhat color is a banana?\n1) Red\n2) Blue\n3) Purple\n4) Yellow.\n\nThen you type your answer (in this case "4" and press enter).')
            os.system('cls')

    #Quiz time
    tryagain = "YES"
    while (tryagain.upper() == "YES"):
        score = 0
        os.system('cls')
        print("Great! let's start! ")
        answer = input("What is the color of the sun?\n1) Blue\n2) Yellow\n3) Purple\n4) Orange\n")
        if (answer == "2"):
            input("Correct! 100 points added to the score!")
            score = score + 100
        else:
            input("Incorrect.")
        os.system('cls')
        answer = input(" What is the capital city of Italy?\n1) Madrid\n2) Paris\n3) Rome\n4) New York\n")
        if (answer == "3"):
            input("Correct! 100 points added to the score!")
            score = score + 100
        else:
            input("Incorrect.")
        os.system('cls')
        answer = input(" What is the actual name of the CPU in IT?\n1) Central Policy Unit\n2) Computer Power User\n3) Central Processing Unit\n4) Cost Per Unit\n")
        if (answer == "3"):
            input("Correct! 100 points added to the score!")
            score = score + 100
        else:
            input("Incorrect.")
        os.system('cls')

        if(score>0):
            input("Congratulations you got "+str(score)+"/ 300")
        else:
            input("Better luck next time :/")
        tryagain = input("Would you like to try again?(Yes or No)")
 