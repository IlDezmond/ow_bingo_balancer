from player import Player
import random
from dataclasses import dataclass

from typing import Optional


@dataclass
class TeamState:
    tank1: Optional[Player] = None
    dd1: Optional[Player] = None
    dd2: Optional[Player] = None
    heal1: Optional[Player] = None
    heal2: Optional[Player] = None

    def increase_all_counters(self):
        self.tank1.tank_counter += 1
        self.dd1.dd_counter += 1
        self.dd2.dd_counter += 1
        self.heal1.heal_counter += 1
        self.heal2.heal_counter += 1

    def return_players(self):
        return [self.tank1, self.dd1, self.dd2, self.heal1, self.heal2]


class Balancer:
    roles_map = {
        'tank': 1,
        'dd': 2,
        'heal': 2,
    }

    def __init__(self, players: list[Player]):
        self.players = players
        self.current_team_state = None

    def init_balance(self):
        self.current_team_state = TeamState(*random.sample(self.players, 5))
        self.current_team_state.increase_all_counters()
        return self.current_team_state.return_players()

    @staticmethod
    def get_least_tank(players):
        return min(players, key=lambda player: player.tank_counter)

    @staticmethod
    def get_least_dd(players):
        return min(players, key=lambda player: player.dd_counter)

    @staticmethod
    def get_least_heal(players):
        return min(players, key=lambda player: player.heal_counter)

    def get_role_index(self):
        tank_index = sum((player.tank_counter * self.players.index(player)) for player in self.players) * 2
        dd_index = sum((player.dd_counter * self.players.index(player)) for player in self.players)
        heal_index = sum((player.heal_counter * self.players.index(player)) for player in self.players)
        role_index = {
            'tank': tank_index,
            'dd': dd_index,
            'heal': heal_index
        }
        return dict(sorted(role_index.items(), key=lambda item: item[1], reverse=True))

    def balance(self):
        players_set = self.players.copy()
        role_index = self.get_role_index()
        for role, r_index in role_index.items():
            count = self.roles_map[role]
            for i in range(count):
                player = getattr(self, f'get_least_{role}')(players_set)
                players_set.remove(player)
                setattr(self.current_team_state, f'{role}{i + 1}', player)

        # self.current_team_state.increase_all_counters()
        return self.current_team_state.return_players()
