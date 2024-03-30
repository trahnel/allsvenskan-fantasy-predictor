import json
import os
import requests

FILES_PATH = '2024/data/during-season/allsvenskan'

bootstrap_static = requests.get(
    'https://fantasy.allsvenskan.se/api/bootstrap-static/')
bootstrap_json = bootstrap_static.json()


os.makedirs(FILES_PATH, exist_ok=True)
with open(f'{FILES_PATH}/bootstrap-static.json', 'w+') as json_file:
    json.dump(bootstrap_json, json_file, indent=2)

players = bootstrap_json['elements']
players_count = len(players)

os.makedirs(f'{FILES_PATH}/players', exist_ok=True)

for player in players:
    player_id = str(player['id'])
    first_name = player['first_name']
    last_name = player['second_name']

    print(
        f'Getting players ({player_id}/{players_count}) {first_name} {last_name}')

    player_response = requests.get(
        f'https://fantasy.allsvenskan.se/api/element-summary/{player_id}/')

    file_name = f"{player_id.rjust(3, '0')}_{first_name}_{last_name}".replace(
        ' ', '_')
    with open(f'{FILES_PATH}/players/{file_name}.json', 'w+') as player_file:
        json.dump(player_response.json(), player_file, indent=2)

print(f'Done! Got {players_count} players.')
