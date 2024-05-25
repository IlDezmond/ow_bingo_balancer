import os

from player import Player
from balancer import Balancer


games = []


def main_balance_process(trimmed_lines, games_counter):
    players = [Player(line) for line in trimmed_lines]
    balancer = Balancer(players)
    current_game = balancer.init_balance()
    games.append(current_game)
    print(current_game)
    for player in players:
        print(
            f'{player.name} - {player.tank_counter=} - {player.dd_counter=} - {player.heal_counter=}'
        )

    for game in range(games_counter - 1):
        current_game = balancer.balance()
        games.append(current_game)
        print(current_game)
        for player in players:
            print(
                f'{player.name} - {player.tank_counter=} - {player.dd_counter=} - {player.heal_counter=}'
            )


def main():
    file_exists = os.path.exists('players.txt')

    if not file_exists:
        input("Не найден файл players.txt.")

    with open('players.txt', 'r') as file:
        raw_data = file.readlines()
        trimmed_lines = [line.strip() for line in raw_data if line.strip()]
        if len(trimmed_lines) != 5:
            input(
                'Количество игроков должно быть равно 5. \n'
                'Текущее количество игроков: ' + str(len(trimmed_lines))
            )

    games_counter = 10  # int(input('Введите количество игр: '))
    main_balance_process(trimmed_lines, games_counter)


if __name__ == '__main__':
    main()
