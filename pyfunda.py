import sys
import random
print("choose any one:\n 1 for rock\n 2 for paper\n3 for scissors")
playerchoice = int(input("enter the value:"))
compchoice = int(random.choice("123"))
print("your choice is "+ str(playerchoice) + ", computer chose "+ str(compchoice)+".")
if playerchoice == 1 and compchoice ==3:
    print("🥳you win!")
elif playerchoice == 2 and compchoice ==1:
    print("🥳you win!")
elif playerchoice == 3 and compchoice ==2:
    print("🥳you win!")        
elif playerchoice==compchoice:
    print("tied game")    
else:
    print("🐍python won")
