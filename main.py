import os

from balancer import Balancer
from player import Player
from openpyxl import Workbook
import sys

games = []


def write_games_to_xlsx(games):
    wb = Workbook()
    ws = wb.active
    ws.append(['Tank', 'DD1', 'DD2', 'Heal1', 'Heal2'])
    for row in games:
        ws.append(list(map(str, row.values())))

    save_flag = False
    counter = 0
    while not save_flag and counter < 100:
        try:
            if counter <= 0:
                counter += 1
                wb.save('games.xlsx')
                save_flag = True
            else:
                counter += 1
                wb.save(f'games{counter}.xlsx')
                save_flag = True
        except PermissionError:
            pass


def main_balance_process(trimmed_lines, games_counter):
    players = [Player(line) for line in trimmed_lines]
    balancer = Balancer(players)
    current_game = balancer.init_balance()
    games.append(current_game)
    # print(current_game)
    # for player in players:
    #     print(
    #         f'{player.name} - {player.tank_counter=} - {player.dd_counter=} - {player.heal_counter=}'
    #     )

    for game in range(games_counter - 1):
        current_game = balancer.balance()
        games.append(current_game)
        # print(current_game)
        # for player in players:
        #     print(
        #         f'{player.name} - {player.tank_counter=} - {player.dd_counter=} - {player.heal_counter=}'
        #     )


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
            sys.exit()

    games_counter = 0
    while games_counter < 1 or games_counter > 500:
        try:
            games_counter = int(input('Введите количество игр: '))
            if games_counter < 1:
                print('Количество игр должно быть больше 0.')
            elif games_counter > 500:
                print('А не дохуя ли?\n')
        except ValueError:
            print('Число введи, дебил!')
    main_balance_process(trimmed_lines, games_counter)
    # print(games)
    write_games_to_xlsx(games)


if __name__ == '__main__':
    main()
