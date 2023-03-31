from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position

DEFAULT_CHARACTER_NAME = "Character"


class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    current_position: tuple = (-100,-100)
    move_count: int = 0

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus
    character: Character
    map: Map

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        self.map = Map()
        self.character.enter_map(map)

    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.character = Character(character_name)
        else:
            self.character = Character(DEFAULT_CHARACTER_NAME)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        self.character.move(direction)

    def set_character_position(self, xycoordinates: tuple) -> None:
        self.character.current_position = Position(xycoordinates[0],xycoordinates[1])
        self.status.current_position = self.character.current_position

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        return self.map.size[0]*self.map.size[1]

    
