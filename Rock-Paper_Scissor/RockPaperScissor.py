import random

def get_choice_from_user():
    while True:
        user_choice = int(input("Choose rock, paper, or scissors: "))
        if user_choice == 1:
            return "rock"
        if user_choice == 2:
            return "paper"
        if user_choice == 3:
            return "scissors"
        else:
            print("Warning: Please choose rock, paper, or scissors.")

def get_choice_from_computer():
    return random.choice(['rock', 'paper', 'scissors'])

def analyze_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_points = 0
    computer_points = 0
    while True:
        print("The choices are:")
        print("[1] Rock ")
        print("[2] Paper ")
        print("[3] Scissors ")
        user_choice = get_choice_from_user()
        computer_choice = get_choice_from_computer()
        print("----------------------------")
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        result = analyze_winner(user_choice, computer_choice)
        print(result)
        print('----------------------------')
        if 'win' in result:
            user_points += 1
        elif 'win' in result.lower():
            computer_points += 1
        
        # Points :-
        print('----------------------------')
        print(f"Player's score: {user_points}\nComputer's score: {computer_points}")
        print('----------------------------')

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
