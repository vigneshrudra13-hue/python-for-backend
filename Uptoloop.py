import sys
import random
playagain =True
while playagain == True:
    print("choose any one:\n1 for rock\n2 for paper\n3 for scissors")
    playerchoice = int(input("enter the value:"))
    compchoice = int(random.choice("123"))
    
    if playerchoice <= 3 and playerchoice != 0:
        print("👉Your choice is "+ str(playerchoice) + "\n👉 computer chose "+ str(compchoice)+".")
        if playerchoice == 1 and compchoice == 3:
            print("🥳 you win!")
        elif playerchoice == 2 and compchoice == 1:
            print("🥳 you win!")
        elif playerchoice == 3 and compchoice == 2:
            print("🥳 you win!")        
        elif playerchoice == compchoice:
            print("😱😱 tied game")    
        else:
            print("🐍python won")
    else:
        print("Invalid option!!")
        
    hey = input("👁️ 👁️ If to continue playing enter:\nY for Yes\nE for Exit\n:")
    if hey.lower() == 'y':
            continue
    else :
            playagain = False   
            for x in "ThankYou" :
                print(x)
         
    