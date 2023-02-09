
#input how many games you want to play
#present who one each round
#tally scores
#present final score and reveal winner


import random 

def rock_paper_scissors():
    computer_score = 0
    player_score = 0
    # while True:
    #     number_of_plays=input("Enter number of times you want to play:")
    #     if number_of_plays in ('rock', 'paper', 'scissors'):
    #         break
    #     else:
    #         print("Please input an integer")
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    # players_choice = input("Choose rock, paper, or scissors:")
    while True:
        players_choice=input("Choose rock, paper, or scissors:").lower()
        if players_choice in ('rock', 'paper', 'scissors'):
            break
        else:
            print('Please choose from the following : rock, paper or scissors')
    print("Computer chose: " + computer_choice)
    results = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
    if results[players_choice] == computer_choice:
        print("Player has won")
    elif results[computer_choice] == players_choice:
        print("Computer has won")
    else:
        print("It's a draw.")

if __name__ == "__main__":
    rock_paper_scissors()

