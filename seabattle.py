import random

def create_ship_positions():
    ship_positions = {}
    for player in players:
        player_name, num_ships = player
        print(f"{player_name}, choose {num_ships} positions for your ships (1-20):")
        positions = []
        for i in range(num_ships):
            while True:
                position = int(input(f"Enter position {i + 1}: "))
                if 1 <= position <= 20 and position not in positions:
                    positions.append(position)
                    break
                else:
                    print("Invalid position. Choose a number between 1 and 20.")
        for position in positions:
            ship_positions[position] = player_name
    return ship_positions

players = [("Maverick", 1), ("Gunner", 2), ("Matilda", 3)]

ship_positions = create_ship_positions()

def computer_bomb_position():
    return random.choice(list(ship_positions.keys()))

def is_game_over():
    return len(ship_positions) == 0

while not is_game_over():
    print("Current state of the game:")
    for position, player in ship_positions.items():
        print(f"Position {position}: Ship owned by {player}")

    computer_bomb = computer_bomb_position()

    if computer_bomb in ship_positions:
        player_hit = ship_positions[computer_bomb]
        print(f"Computer bombed position {computer_bomb} and hit {player_hit}'s ship!")
        del ship_positions[computer_bomb]
    else:
        print(f"Computer bombed position {computer_bomb} and missed!")

print("Game Over!")
print(f"{player_hit} is the winner!")

