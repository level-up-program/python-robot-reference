from typing import Tuple


class Position:
    coordinates: Tuple[int, int]

    def __init__(self, x: int, y: int):
        self.coordinates = (x, y)

    def __eq__(self, o):
        return (
            self.coordinates[0] == o.coordinates[0]
            and self.coordinates[1] == o.coordinates[1]
        )

    def __str__(self):
        return f"{self.coordinates}"
