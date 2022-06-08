from enum import Enum
from dataclasses import dataclass
from levelup.character import Player

DEFAULT_PLAYER_NAME = "Player"
ARBITRARY_INVALID_INITIALIZED_POSITION = (-1,-1)


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    player: Player = Player(DEFAULT_PLAYER_NAME)
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_player(self, player_name: str) -> None:
        if not player_name:
            player_name = DEFAULT_PLAYER_NAME
        self.status.player = Player(player_name)

    def move(self, direction: Direction) -> None:
        print(f"Moved {direction.name}")

    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")

