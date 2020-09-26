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
    #while (player_input != "R" ) or (player_input != "P" ) or (player_input != "S") :
        #player_input = input("Invalid input please try again")
    #cant get the validation to work
    if player_input == computer:
        print("Tie!")
    elif (player_input =="R" and computer=="S") or (player_input =="S" and computer=="P") or (player_input =="P" and computer=="R"):
        print("You win!", player_input, "beats", computer)
        loop =True
    else:
        print("You lose!", computer, "beats", player_input, ",try again.")


    computer = options[randint(0,2)]
