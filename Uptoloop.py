import sys
import random

def rps():
    x = input("do you wanna play rock paper scissors?\ny for Yes \n n for No:")
    if x.lower() == 'y':
        playagain = True
    else:
        playagain = False
        print('Cool!\nhave a nice day')
        sys.exit()
    gamecount = 0
    playerwin=0
    pythonwin=0
    while playagain == True:
        gamecount += 1
        print("choose any one:\n1 for rock\n2 for paper\n3 for scissors")
        playerchoice = int(input("enter the value:"))
        compchoice = int(random.choice("123"))
        
        if playerchoice <= 3 and playerchoice != 0:
            print("👉 Your choice is "+ str(playerchoice) + "\n👉 computer chose "+ str(compchoice)+".")
            if playerchoice == 1 and compchoice == 3:
                print("🥳 you win!")
                playerwin +=1
            elif playerchoice == 2 and compchoice == 1:
                print("🥳 you win!")
                playerwin +=1
            elif playerchoice == 3 and compchoice == 2:
                print("🥳 you win!")
                playerwin +=1        
            elif playerchoice == compchoice:
                print("😱😱 tied game")    
            else:
                print("🐍python won")
                pythonwin += 1
        else:
            print("Invalid option!!")
        y = f"you've played {gamecount} games , and won {playerwin} times,but python won {pythonwin} times"   
        print(y)
        hey = input("👁️ 👁️ If to continue playing enter:\nY for Yes\nE for Exit\n:")
        if hey.lower() == 'y':
            continue
        else:
            playagain = False   
            for x in "ThankYou":
                print(x)


if __name__ == '__main__':
    rps()    
    