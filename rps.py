def display_header():
    print("\nROCK ... ")
    print("PAPER ... ")
    print("SCISSORS ... \n")

def player_choice():
    #player 1
    player1 = input("Enter player one's choice: ")

def calculate_winner():
    #player2
    player2 = input("Enter player two's choice: ")
    #1=rock 2=scissors
    if player1 == "rock" and player2 == "scissors":
        print("player one wins! ")
    #1=paper 2=scissors
    elif player1 == "paper" and player2 == "scissors":
        print("player two wins! ")
    #1=2 tie scenario
    elif player1 == player2:
        print("YOU TIED! ")
    #1=rock 2=paper
    elif player1 == "rock" and player2 == "paper":
        print("player two wins! ")
    #1=scissors 2=paper
    elif player1 == "scissors" and player2 == "paper":
        print("player one wins! ")
    #1=paper 2=rock
    elif player1 == "paper" and player2 == "rock":
        print("player one wins! ")
    #1=scissors 2=rock
    elif player1 == "scissors" and player2 == "rock":
        print("player two wins! ")
    else:
        print("something went wrong")

