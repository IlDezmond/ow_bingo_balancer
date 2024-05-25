class Player:
    def __init__(self, name, tank_counter=0, dd_counter=0, heal_counter=0):
        self.name = name
        self.tank_counter = tank_counter
        self.dd_counter = dd_counter
        self.heal_counter = heal_counter

    def __repr__(self):
        return self.name
