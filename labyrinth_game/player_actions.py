from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")


def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    room = ROOMS[game_state['current_room']]
    if direction not in room['exits']:
        print("Нельзя пойти в этом направлении.")
        return

    next_room = room['exits'][direction]

    if (next_room == 'treasure_room'
            and 'rusty_key' not in game_state['player_inventory']):
        print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
        return
    elif next_room == 'treasure_room' and 'rusty_key' in game_state['player_inventory']:
        print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")

    game_state['current_room'] = next_room
    game_state['steps_taken'] += 1

    describe_current_room(game_state)
    random_event(game_state)


def take_item(game_state, item_name):
    room = ROOMS[game_state['current_room']]
    if item_name == 'treasure_chest':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    
    if item_name in room['items']:
        room['items'].remove(item_name)
        game_state['player_inventory'].append(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
        return

    if item_name == 'torch':
        print("Вы зажгли факел. Стало светлее.")
    elif item_name == 'sword':
        print("Вы чувствуете прилив уверенности.")
    elif item_name == 'bronze_box':
        if 'rusty_key' not in game_state['player_inventory']:
            print("Вы открыли бронзовую шкатулку и нашли ржавый ключ!")
            game_state['player_inventory'].append('rusty_key')
        else:
            print("Шкатулка пуста.")
    else:
        print("Вы не знаете, как использовать этот предмет.")