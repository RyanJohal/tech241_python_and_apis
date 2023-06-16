
import requests
from random import randint

post_codes_req = requests.get("https://api.postcodes.io/postcodes/sl61tx")

def fetch_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            "name": pokemon_data["name"],
            "health": pokemon_data["stats"][0]["base_stat"],
            "damage": randint(1, 10)
        }
    else:
        return None

def attack():
    roll_to_attack = randint(0, 3)
    return roll_to_attack

def defend():
    roll_to_defend = randint(0, 3)
    return roll_to_defend

while True:
    # Game set up
    player1_pokemon = input("Player1: select a Pokemon: ")
    player1_info = fetch_pokemon_info(player1_pokemon.lower())
    if not player1_info:
        print("Invalid Pokemon name. Please try again.")
        continue

    print(f"Player1: {player1_info['name']}")

    player2_pokemon = input("\nPlayer2: select a Pokemon: ")
    player2_info = fetch_pokemon_info(player2_pokemon.lower())
    if not player2_info:
        print("Invalid Pokemon name. Please try again.")
        continue

    print(f"Player2: {player2_info['name']}\n")

    player1_hp = player1_info["health"]
    player2_hp = player2_info["health"]

    game_on = True

    while game_on:
        print(f"\nPlayer1 current health: {player1_hp}")
        print(f"Player2 current health: {player2_hp}\n")

        # Player1 Turn
        if player1_hp <= 0:
            print("Game over! Player2 wins")
            game_on = False
        else:
            print("Player1 Attack Turn")
            attack_roll = attack()
            print(f"Your roll: {attack_roll}")

            defend_roll = defend()
            print(f"Player2's roll: {defend_roll}")

            if attack_roll > defend_roll:
                damage = (attack_roll - defend_roll) + player1_info['damage']
                player2_hp -= damage
                print(f"{damage} damage inflicted! Player2's health point: {player2_hp}")
            elif attack_roll == defend_roll:
                print("No damage!")
            else:
                player1_hp -= 1
                print(f"1 damage taken, your health point: {player1_hp}")

        # Player2 Turn
        if player2_hp <= 0:
            print("Game over! Player1 wins")
            game_on = False
        else:
            print(f"\nPlayer2 Attack Turn")
            attack_roll = attack()
            print(f"Your roll: {attack_roll}")

            defend_roll = defend()
            print(f"Player1's roll: {defend_roll}")

            if attack_roll > defend_roll:
                damage = (attack_roll - defend_roll) + player2_info['damage']
                player1_hp -= damage
                print(f"{damage} damage inflicted! Player1's health point: {player1_hp}")
            elif attack_roll == defend_roll:
                print("No damage!")
            else:
                player2_hp -= 1
                print(f"1 damage taken, your health point: {player2_hp}")

    next_game = input("\nWould you like to play again? (yes/no): ")
    if next_game != "yes":
        break
