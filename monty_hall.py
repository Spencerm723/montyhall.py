import random

num_simulations = int(input("How many games to simulate? "))

stay_wins = 0
switch_wins = 0

for _ in range(num_simulations):
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    player_choice = random.randint(0, 2)

    host_opens = next(
        i for i in range(3)
        if i != player_choice and doors[i] == "goat"
    )

    remaining_door = 3 - player_choice - host_opens

    if doors[player_choice] == "car":
        stay_wins += 1
    else:
        switch_wins += 1

print(f"\nStaying wins: {stay_wins}")
print(f"Switching wins: {switch_wins}")
print(f"Switching wins {switch_wins / num_simulations * 100:.2f}% of the time!")