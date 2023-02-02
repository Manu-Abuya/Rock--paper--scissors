# Rock, Paper, Scissors Game

# Define the options for the game
options = ["rock", "paper", "scissors"]

# Function to check the winner of the game
def check_winner(player1, player2):
    
    # Check if it's a draw
    if player1 == player2:
        return "Draw"
    
    # Check for Rock
    elif player1 == "rock":
        if player2 == "scissors":
            return "Player 1 wins"
        else:
            return "Player 2 wins"
        
    # Check for Paper
    elif player1 == "paper":
        if player2 == "rock":
            return "Player 1 wins"
        else:
            return "Player 2 wins"
        
    # Check for Scissors
    elif player1 == "scissors":
        if player2 == "paper":
            return "Player 1 wins"
        else:
            return "Player 2 wins"
        
    # If an invalid option is entered
    else:
        return "Invalid option, please enter a valid option."

# Main function to play the game
def play_game():
    
    # Get player 1's choice
    player1 = input("Player 1, enter your choice: rock, paper, or scissors: ").lower()
    # Check if player 1's choice is valid
    if player1 not in options:
        print("Invalid option, please enter a valid option.")
        return
    
    # Get player 2's choice
    player2 = input("Player 2, enter your choice: rock, paper, or scissors: ").lower()
    # Check if player 2's choice is valid
    if player2 not in options:
        print("Invalid option, please enter a valid option.")
        return
    
    # Get the winner
    winner = check_winner(player1, player2)
    # Print the winner
    print(winner)

# Play the game
play_game()

