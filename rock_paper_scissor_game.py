import random

print("\nWelcom to Rock/Paper/Scissor Game\n")
print("\nR for Rock\nP for Paper\nS for Scissor\n")
playerName = input("\nEnter your name: ")

user_score = 0
comp_score = 0
tie = 0
attempts = 0

options = ["R", "P", "S"]

while (attempts <= 10):
    user_input = input("\nChoose any: ").upper()
    comp_input = random.choice(options)

    if user_input not in options:
        print("Invalid enter try again!")
        quit()

    if user_input == comp_input:
        print(f"Game Tie\n{playerName} chose: {user_input} Computer chose: {comp_input}")
        tie += 1

    elif user_input == 'R' and comp_input == 'S':
        print(f"You won!\n{playerName} chose: {user_input} Computer chose: {comp_input}")
        user_score += 1

    elif user_input == 'P' and comp_input == 'R':
        print(f"You won!\n{playerName} chose: {user_input} Computer chose: {comp_input}")
        user_score += 1

    elif user_input == 'S' and comp_input == 'P':
        print(f"You won!\n{playerName} chose: {user_input} Computer chose: {comp_input}")
        user_score += 1

    else:
        print(f"Computer won!\n{playerName} chose: {user_input} Computer chose: {comp_input}")
        comp_score += 1

    attempts += 1 

if user_score > comp_score:
    print("\nGame Finished! \nYou won the game\nYou got ",user_score," score\nComputer got ",comp_score," score\n")
elif user_score == comp_score:
    print("\nGame Tie! \nYou got ",user_score, " score\nComputer got ",comp_score," score\n")
else:
    print("\nGame Finished! \nComputer won the game\nYou got ",user_score," score\nComputer got ",comp_score," score\n")
