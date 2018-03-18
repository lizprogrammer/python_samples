import random

outcomes = ["rock", "paper", "scissors"]

while True:
    player1 = outcomes[random.randrange(0, 3)]
    player2 = outcomes[random.randrange(0, 3)]
    print(player1 + " " + player2)
    the_winner = ""
    if player1 == player2:
        the_winner = "tie"
    elif(player1 == "paper"
         and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        the_winner = player1
    else:
        the_winner = player2
    print("the winner is: " + the_winner)
    go_again = input("Again? ")
    if go_again == "n":
        break

print("goodbye")
