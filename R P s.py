from random import randint
#function that randomly selects integers

options = ["R", "P", "S"]

#assigns a random int to options to randomise the computers selection
computer = options[randint(0,2)]

#set player to False
loop = False
#allows for the loop to progress
while loop == False:

    player_input = input("R, P Or S")
    if player_input == computer:
        print("Tie!")
    elif player_input == "R":
        if computer == "P":
            print("You lose!", computer, "beats", player_input,",try again.")
        else:
            print("You win!", player_input, "beats", computer)
            loop = True
    elif player_input == "P":
        if computer == "S":
            print("You lose!", computer, "beats", player_input,",try again.")
        else:
            print("You win!", player_input, "beats", computer)
            loop = True
    elif player_input == "S":
        if computer == "R":
            print("You lose...", computer, "beats", player_input,",try again.")
        else:
            print("You win!", player_input, "beats", computer, ",try again.")
            loop = True
    else:
        print("Invalid Input")
    #player was set to True, but we want it to be False so the loop continues
    computer = options[randint(0,2)]
