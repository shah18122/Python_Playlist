import random

p1_score = 0
p2_score = 0
winning_score = 5

print("First to 5 wins!")

while p1_score < winning_score and p2_score < winning_score:
    player1 = input("\nEnter your choice (Rock, Paper, or Scissors): ").capitalize()
    while player1 not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please try again.")
        player1 = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()

    player2 = random.choice(["Rock", "Paper", "Scissors"])
    print("Player 2 (Computer):", player2)

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "Rock" and player2 == "Scissors") or \
         (player1 == "Paper" and player2 == "Rock") or \
         (player1 == "Scissors" and player2 == "Paper"):
        print("Player 1 wins this round!")
        p1_score += 1
    else:
        print("Player 2 wins this round!")
        p2_score += 1

    print("Score -> Player 1:", p1_score, "| Player 2:", p2_score)

if p1_score == winning_score:
    print("\nPlayer 1 wins the game!")
else:
    print("\nPlayer 2 wins the game!")
