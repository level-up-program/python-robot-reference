from levelup.character import Character
from levelup.direction import Direction

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

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.character = Character(character_name)
        else:
            self.character = Character(DEFAULT_CHARACTER_NAME)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        pass

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
