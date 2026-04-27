class playerstats:
    def __init__(self, Name, ovrgames, category):
        self.name = Name
        self.tgames = ovrgames
        self.cat = category
        if self.cat.lower() == 'batsman':
            self.Batsman()
        elif category.lower() == 'bowler':
            self.Bowler()    
    def Batsman(self):
        Date = input("Enter today's date: ")
        CMR = int(input("Enter the runs you've scored: "))
        CMI = int(input("Enter the innings played: "))
        CMW = int(input("Enter the wickets you've taken if any: "))
        Avg = CMR/CMI if CMI !=0 else 0.0 
        data = f"Date:{Date}\nRuns Scored:{CMR}\nInnings played:{CMI}\nBatting average:{Avg:.2f}\nWickets taken:{CMW}\n\n"
        filename = f"{self.name}_Batsman.txt"
        Choice = input("enter if you want to over write the file or edit the file\nY for Yes (or) N for NO")
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(data)
        else:   
            with open(filename,'w') as f:
                f.write(data)
        ch = input("You wanna preview your file?\nY for yes and N for no:")
        if ch.lower() == 'y':
            with open(filename,'r') as f :
                print("total history:")
                print(f.read())
        else:
            print("Thanks for the update!!")
            print("Your data has been saved!!")
        print(f"A player account has been created with {self.name} as name and in {self.cat} category\n")
        
    def Bowler(self):
        Date = input("Enter today's date: ")
        CMR = int(input("Enter the runs you've scored if any: "))
        CMI = int(input("Enter the innings played if any: "))
        CMC = int(input("How many runs have you conceded:"))
        CMW = int(input("Enter the wickets you've taken: "))
        Avg = CMC / CMW if CMW != 0 else print("NO net bowling avg")
        data = f"Date:{Date}\nRuns Scored:{CMR}\nInnings played:{CMI}\nBowling average:{Avg:.2f}\nWickets taken:{CMW}\n"
        filename = f"{self.name}_Bowler.txt"
        Choice = input("enter if you want to over write the file or edit the file\nY for Yes (or) N for NO")
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(data)
        else:   
            with open(filename,'w') as f:
                f.write(data)
        ch = input("You wanna preview your file?\nY for yes and N for no:")
        if ch.lower() == 'y':
            with open(filename,'r') as f :
                print("total history:")
                print(f.read())
        else:
            print("Thanks for the update!!")
            print("Your data has been saved!!")
        print(f"A player account has been created with {self.name} as name and in {self.cat} category\n")

        
if __name__ == '__main__':
    p1 = input("enter player name: ")
    g = int(input("no. of games: "))
    cat = input("Your role[Batsman,Bowler]: ")

    L = playerstats(p1, g, cat)
