start = input("Do you wan to start the game? y/n: ")

def start_game():
    if start == "yes":
        print("Initialization Complete")
    else:
        print("Initialization Failed")
        
start_game()