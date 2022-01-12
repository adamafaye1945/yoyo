choice_1="rock"
choice_2= "paper"
choice_3="scissor"

player_1_input=input("player1, write down what you choose")
player_2_input=input("player2, write down what you choose")

#below is a code where there is a tie
if player_1_input==player_2_input:
    print("this a tie")

while player_1_input==choice_1: 
    if player_2_input==choice_2:
        print("player 2 wins")
        break
    elif player_2_input==choice_3:
        print("player 1 wins")
        break
    
while player_1_input==choice_2:
    if player_2_input==choice_3:
        print("player 2 wins")
        break
    elif player_2_input==choice_1:
        print("player 1 wins")
        break

while player_1_input==choice_3:
    if player_2_input==choice_1:
        print("player 2 wins")
        break
    elif player_2_input==choice_2:
        print("player 1 wins")
        break
print("do you want to start a new game")
