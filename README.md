# Текстовая игра "Лабиринт сокровищ"

Добро пожаловать в "Лабиринт сокровищ" — текстовую приключенческую игру на Python!

Ссылка на запись: https://asciinema.org/a/P0gm5VVOZPsjxep4

### Ключевые функции

* `main()` — запускает игру, игровой цикл, обрабатывает ввод игрока  
* `process_command(game_state, command)` — обрабатывает команды игрока  
* `describe_current_room(game_state)` — выводит описание комнаты  
* `move_player(game_state, direction)` — перемещение игрока  
* `take_item(game_state, item_name)` — поднятие предмета  
* `show_inventory(game_state)` — вывод инвентаря  
* `use_item(game_state, item_name)` — использование предмета  
* `solve_puzzle(game_state)` — решение загадок  
* `attempt_open_treasure(game_state)` — проверка условия победы  
* `trigger_trap(game_state)` — срабатывание ловушек  
* `random_event(game_state)` — случайные события  
* `show_help(COMMANDS)` — вывод доступных команд  

---

## ⚙ Установка и запуск

```bash
git clone 
cd labyrinth_game
make install

#запуск игры
make project
```

### Игровые команды
* `go <direction>` — перемещение (north/south/east/west)
* `<direction>` — краткая команда для перемещения
* `look — осмотреть текущую комнату
* `take <item>` — поднять предмет
* `use <item>` — использовать предмет из инвентаря
* `inventory` — показать инвентарь
* `solve` — попытаться решить загадку в комнате
* `quit` — выйти из игры
* `help` — показать доступные команды

