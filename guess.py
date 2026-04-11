import sys
import random
import argparse

parser = argparse.ArgumentParser(
        description="A guessing game"
    )
parser.add_argument(
        "-n","--name",metavar="Name",
        required=True,help="Name of the player"
    )
args = parser.parse_args()

def guess(name):
    playerwins = 0
    gamecount = 0
    playagain = True
    
    while playagain:
        print(f"{name}, guess the number Python is thinking: 1, 2, or 3?")
        playerchoice = input("What's your guess?: ")
        compchoice = random.choice("123")
        gamecount += 1
        
        if playerchoice == compchoice:
            print(f"{name}, your guess is spot on! The number was {compchoice}")
            playerwins += 1
        else:
            print(f"{name}, uh oh!! Wrong guess. The number was {compchoice}")
        
        winpercentage = (playerwins / gamecount) * 100
        print(f"Your winning percentage is {winpercentage:.1f}% ({playerwins}/{gamecount})")
        
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            playagain = False
    
    print(f"Thanks for playing, {name}!")

guess(args.name)
    