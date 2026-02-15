command = ""
started=False
while command !="quit":
    command=input("> ").lower()
    if command == "start":
        if started:
            print("car has already started!")
        else:
            started=True
            print("car has started")
    elif command == "stop":
        
        if not started:
            print("car is already stopped!")
        else:
            started=False
            print("car has stopped")
    elif command =="help":
        print("enter start to start the car \nstop to stop the car\nhelp for details\nquit")
    else :
        print("operation exited")
        break