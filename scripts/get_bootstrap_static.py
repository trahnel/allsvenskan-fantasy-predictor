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
