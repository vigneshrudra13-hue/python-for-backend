class playerstats:
    def __init__(self, Name, category):
        self.name = Name
        self.cat = category
        self.track()
        if self.cat.lower() == 'batsman':
            self.Batsman()
        elif self.cat.lower() == 'bowler':
            self.Bowler()    
        else :
            self.Allrounder()    
    def track(self):
        Date = input("Enter today's date: ")
        CMR = int(input("Enter the runs you've scored: "))
        CMI = int(input("Enter the innings played: "))
        CMW = int(input("Enter the wickets you've taken if any: "))
        CMC = int(input("How many runs have you conceded:"))
        Avg = CMR/CMI if CMI !=0 else 0.0 
        BAvg = CMC / CMW if CMW != 0 else 0.0
        self.data = f"Date:{Date}\nRuns Scored:{CMR}\nInnings played:{CMI}\nBatting average:{Avg:.2f}\nWickets taken:{CMW}\n\n"
    def Batsman(self):
        Choice = input("enter if you want to over write the file or add data into already existing file the file\nY for Yes (or) N for NO")
        filename = f"{self.name}_Batsman.txt"
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(self.data)

        else:   
            
            with open(filename,'w') as f:
                f.write(self.data)
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
        Choice = input("enter if you want to over write the file or edit the file\nY for Yes (or) N for NO")
        filename = f"{self.name}_Bowler.txt"
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(self.data)
        else:   
            with open(filename,'w') as f:
                f.write(self.data)
        ch = input("You wanna preview your file?\nY for yes and N for no:")
        if ch.lower() == 'y':
            with open(filename,'r') as f :
                print("total history:")
                print(f.read())
        else:
            print("Thanks for the update!!")
            print("Your data has been saved!!")
        print(f"A player account has been created with {self.name} as name and in {self.cat} category\n")

    def Allrounder(self):
        Choice = input("enter if you want to over write the file or add data into already existing file the file\nY for Yes (or) N for NO")
        
        filename = f"{self.name}_ALLrounder.txt"
        
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(self.data)
        else:   
            with open(filename,'w') as f:
                f.write(self.data)
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
    cat = input("Your role[Batsman,Bowler]: ")

    L = playerstats(p1, cat)
