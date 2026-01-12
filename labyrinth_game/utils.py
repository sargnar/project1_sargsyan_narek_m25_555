import math

from labyrinth_game.constants import ROOMS


def describe_current_room(game_state):
    room = ROOMS[game_state['current_room']]
    print(f"\n== {game_state['current_room'].upper()} ==")
    print(room['description'])

    if room['items']:
        print("Заметные предметы:", ", ".join(room['items']))
    if room['exits']:
        print("Выходы:", ", ".join(room['exits'].keys()))
    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    room = ROOMS[game_state['current_room']]
    if not room['puzzle']:
        print("Загадок здесь нет.")
        return

    question, answer = room['puzzle']
    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()

    alternatives = {
        '10': ['10', 'десять', 'дсять'],
        'шаг шаг шаг': ['шагшаг шаг', 'шагшагшаг'],
        'резонанс': ['резонанс']
    }

    valid_answers = alternatives.get(answer, [answer])

    if user_answer in valid_answers:
        print("Загадка решена!")
        room['puzzle'] = None

        if game_state['current_room'] == 'hall':
            print("Вы получаете ключ от сокровищницы!")
            if 'treasure_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('treasure_key')
        elif game_state['current_room'] == 'library':
            print("Вы находите редкий свиток.")
            game_state['player_inventory'].append('ancient_scroll')
        elif game_state['current_room'] == 'trap_room':
            print("Ловушка обезврежена")
    else:
        print("Неверно.")
        if game_state['current_room'] == 'trap_room':
            trigger_trap(game_state)


def attempt_open_treasure(game_state):
    room = ROOMS[game_state['current_room']]
    if game_state['current_room'] != 'treasure_room':
        print("Здесь нечего открывать.")
        return

    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
        return

    print("Сундук заперт. Ввести код? (да/нет)")
    choice = input().strip().lower()
    if choice == 'да':
        code = input("Введите код: ").strip()
        _, correct_code = room['puzzle']
        if code == correct_code:
            print("Код верный! Сундук открыт, вы победили!")
            room['items'].remove('treasure_chest')
            game_state['game_over'] = True
        else:
            print("Неверный код.")
    else:
        print("Вы отступаете от сундука.")


def show_help(COMMANDS):
    print("\nДоступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd.ljust(16)} - {desc}")


def pseudo_random(seed, modulo):
    x = math.sin(seed * 12.9898) * 43758.5453
    frac = x - math.floor(x)
    return int(frac * modulo)


def trigger_trap(game_state):
    print("Ловушка активирована! Пол дрожит под ногами...")
    inventory = game_state['player_inventory']
    if inventory:
        idx = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(idx)
        print(f"Вы уронили {lost_item}")
    else:
        danger = pseudo_random(game_state['steps_taken'], 10)
        if danger < 3:
            print("Вы погибли.")
            game_state['game_over'] = True
        else:
            print("Вы уцелели")


def random_event(game_state):
    roll = pseudo_random(game_state['steps_taken'], 10)
    if roll != 0:
        return

    event_type = pseudo_random(game_state['steps_taken'] + 1, 3)

    room = ROOMS[game_state['current_room']]
    inv = game_state['player_inventory']

    if event_type == 0:
        print("Вы находите монетку на полу.")
        room['items'].append('coin')
    elif event_type == 1:
        print("Вы слушите шорох")
        if 'sword' in inv:
            print("Вы отпугнули существо мечом.")
    elif event_type == 2:
        if game_state['current_room'] == 'trap_room' and 'torch' not in inv:
            print("Опасно!")
            trigger_trap(game_state)