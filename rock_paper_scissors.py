import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(choices):
    player = choices["player"]
    comp = choices["computer"]
    loose = "You Loose"
    win = "You WIN!"
    rock_smashes_scissors = "Rock smashes scissors!"
    paper_cover_rock = "Paper cover rock!"
    scissors_cut_paper = "Scissor cut paper!"
    print(f"Player choice -\t{choices["player"].upper()}\nComputer choice -\t{choices["computer"].upper()}")
    if player == comp:
        return "It's a tie!"
    elif player == "rock":
        if comp == "scissors":
            return f"{rock_smashes_scissors} {win}"
        else:
            return f"{paper_cover_rock} {loose}"
    elif player == "paper":
        if comp == "rock":
            return f"{paper_cover_rock} {win}"
        else:
            return f"{scissors_cut_paper} {loose}"
    elif player == "scissors":
        if comp == "paper":
            return f"{scissors_cut_paper} {win}"
        else:
            return f"{rock_smashes_scissors} {loose}"

result = check_win(get_choices())
print(result)