from levelup.map import Map
from levelup.character import Character
from levelup.direction import Direction
from levelup.position import Position

class CharacterDouble (Character):

    is_move_called = False
    is_enter_map_called = False
    last_move_direction = None

    def __init__(self, character_name):
        # This will make a CharacterDouble that is on position 5,5. Is there refactoring you can do here to make it clearer that 5,5 is arbitrary?
        self.current_position = Position(5,5)

    def move(self, direction: Direction) -> None:
        # What should happen here so we can keep track of calls to this and use it in our tests?
        pass

    def enter_map(self, map: Map) -> None:
        # What should happen here so we can keep track of calls to this and use it in our tests?
        pass
