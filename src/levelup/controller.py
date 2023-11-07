from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position




class GameStatus:
    character_name: str = ""
    current_position: tuple = (-100,-100)
    move_count: int = 0

    def __str__(self) -> str:
        return f"{self.character_name} is currently on {self.current_position} and moved {self.move_count} times."

class GameController:
    status: GameStatus
    character: Character
    map: Map

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        # TODO: implement method here and remove the print statement below
        print("start_game method not yet implemented")            

        # Status code is written for you
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = 0

    # Pre-written for you
    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        # TODO: implement method here and remove the print statement below
        print("move method not yet implemented")

        # Status code is written for you
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = self.status.move_count + 1

    ## ************************************************
    ## METHODS THAT EXIST JUST TO HELP WITH TESTING -- PREWRITTEN FOR YOU
    ## ************************************************
    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        return self.map.num_positions
    
    def initalize_game_for_testing(self) -> None:
        self.create_character("")
        self.start_game()

    
