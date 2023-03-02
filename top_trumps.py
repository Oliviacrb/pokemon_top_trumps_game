import random
import requests

player_wins = 0
computer_wins = 0

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def run():

    global player_wins, computer_wins

    player_won = False

    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('Stats:')
    print('ID:{}'.format(my_pokemon['id']))
    print('Height:{}'.format(my_pokemon['height']))
    print('Weight:{}'.format(my_pokemon['weight']))
    stat_choice = input('Which stat do you want to use? (id, height, weight)')
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]


    if my_stat > opponent_stat:
        print('You Win!')
        player_wins = player_wins + 1
        player_won = True
        print('\n')
    elif my_stat < opponent_stat:
        print('You Lose!')
        computer_wins = computer_wins + 1
        print('\n')
    else:
        print('Draw!')
        print('\n')
    return player_won


game_counter = 0
number_of_wins = 0

while game_counter < 5:
    game_counter = game_counter + 1
    win = run()

if player_wins > computer_wins:
    print('You have won. Final score: {}-{}'.format(player_wins, computer_wins))
elif player_wins < computer_wins:
    print('You have lost. Final score: {}-{}'.format(player_wins, computer_wins))