class playerstats:
    def __init__(self, Name, ovrgames, category):
        self.name = Name
        self.tgames = ovrgames
        self.cat = category

        CMR = int(input("Enter the runs you've scored: "))
        CMB = int(input("Enter the innings played: "))
        CMW = int(input("Enter the wickets you've taken if any: "))
        Date = input("Enter today's date: ")

        # replicate original behavior: Avg = runs / balls (avoid division by zero)
        Avg = CMR / CMB if CMB != 0 else 0.0

        data = f"Date:{Date}\nRuns Scored:{CMR}\nBalls faced:{CMB}\nBatting average:{Avg:.2f}\nWickets taken:{CMW}\n"
        filename = f"{self.name}_cricket.txt"
        Choice = input("enter if you want to over write the file or edit the file\nY for Yes (or) N for NO")
        if Choice.lower() == 'n':
            with open(filename, 'a') as f:
                f.write(data)
                
            print("Your data has been saved!!")
            print(f"A player account has been created with {self.name} as name and in {self.cat} category")
            
        else:
            with open(filename,'w') as f:
                f.write(data)
                
        with open(filename,'r') as f :
            print("total history:")
            print(f.read())
if __name__ == '__main__':
    p1 = input("enter player name: ")
    g = int(input("no. of games: "))
    cat = input("Your role: ")

    L = playerstats(p1, g, cat)
