# As my first exercise with Python, I will develope a "Rock, Scissors or Paper" game.
import random

# Variables
choices = ["rock", "scissors", "paper"]
round = 1
player_score = 0
cpu_score = 0

# Function


def shot_result(user, cpu):
    print(f"{user} vs {cpu}\n")
    global player_score
    global cpu_score
    if user == "rock" and cpu == "scissors":
        print(f"{player_name} win this round!!")
        player_score += 1
        return
    elif user == "rock" and cpu == "paper":
        print("CPU win this round!!")
        cpu_score += 1
        return
    elif user == "paper" and cpu == "rock":
        print(f"{player_name} win this round!!")
        player_score += 1
        return
    elif user == "paper" and cpu == "scissors":
        print("CPU win this round!!")
        cpu_score += 1
        return
    elif user == "scissors" and cpu == "paper":
        print(f"{player_name} win this round!!")
        player_score += 1
        return
    elif user == "scissors" and cpu == "rock":
        print("CPU win this round!!")
        cpu_score += 1
        return
    else:
        print("Tie!!\n")
        return


print("Welcome to rock,paper or scissors\n Win the game the best of 5 rounds.")
player_name = input("Enter your name: ")

# While loop
while player_score < 3 and cpu_score < 3:
    print(f'''
        Your score: {player_score}
        CPU score: {cpu_score}
    ''')
    print(f"Round {round}")
    print('''
    1. Rock
    2. Scissors
    3. Paper
    ''')
    selected = input("Select your choice: ")
    cpu_shot = random.choice(choices)
    round += 1
    shot_result(choices[int(selected)-1], cpu_shot)
else:
    print(f'''
        Your score: {player_score}
        CPU score: {cpu_score}
    ''')
    if player_score > cpu_score:
        print(f"{player_score} win the game!!")
    else:
        print("CPU win the game!!")
