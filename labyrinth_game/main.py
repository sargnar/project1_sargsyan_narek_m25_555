#!/usr/bin/env python3
from labyrinth_game.constants import COMMANDS
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def process_command(game_state, command_line):
    parts = command_line.strip().split()
    if not parts:
        return
    command = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None

    directions = ['north', 'south', 'east', 'west']

    match command:
        case 'go':
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление.")
        case c if c in directions:
            move_player(game_state, c)
        case 'look':
            describe_current_room(game_state)
        case 'take':
            if arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет.")
        case 'use':
            if arg:
                use_item(game_state, arg)
            else:
                print("Укажите предмет.")
        case 'inventory':
            show_inventory(game_state)
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case 'help':
            show_help(COMMANDS)
        case 'quit' | 'exit':
            print("Выход из игры.")
            game_state['game_over'] = True
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    describe_current_room(game_state)

    while not game_state['game_over']:
        command = get_input("> ")
        process_command(game_state, command)

main()
  