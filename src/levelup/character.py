from levelup.position import Position
from levelup.controller import Direction
from levelup.map import Map

class Character:
    name = ""
    current_position :Position = None
    map :Map = None

    def __init__(self, character_name):
        self.name = character_name

    def move(self, direction :Direction) -> None:
        self.current_position = self.map.calculate_new_position(
            self.current_position, direction)
    
    def enter_map(map :Map):
        pass
