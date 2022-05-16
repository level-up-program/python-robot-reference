from enum import Enum, auto
from dataclasses import dataclass
from levelup.character import Player

DEFAULT_PLAYER_NAME = "Player"


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@dataclass
class GameStatus:
    player: Player = Player(DEFAULT_PLAYER_NAME)


class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_player(self, player_name: str):
        if not player_name:
            player_name = DEFAULT_PLAYER_NAME
        self.status.player = Player(player_name)

    def move(self, direction: Direction):
        pass
