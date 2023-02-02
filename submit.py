import json
import os
from matrix import update_seat_matrix
from dataclasses import asdict
from seats import Show

def submit(show:Show, username:str):
    update_seat_matrix(show)
    
    with open('selected_seats.json', 'r') as file:
        save_tickets_to_user(show, username, json.load(file))

    _empty()

def _empty() -> None:
    # empty the file for next use
    with open('selected_seats.json', 'w') as file:
        file.write("[]")

def save_tickets_to_user(show:Show, username:str, seats:list) -> None:
    print(show.name, username, seats)
    user = {
        'name': username,
        'history': [
            {
                'show': asdict(show),
                'seats': seats
            }
        ]
    }
    data = get_user_data()
    if user['name'] not in data:
        data[user['name']] = user
    else:
        data[user['name']]['history'].append(user['history'][0])
    with open('users.json', 'w+') as file:
        json.dump(data, file, indent=4)

def get_user_data() -> dict:
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as file:
            file.write('{}')
    with open('users.json', 'r') as file:
        data = json.load(file)
    return data
