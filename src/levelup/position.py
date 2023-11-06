class Position ():

    x = -100
    y = -100

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Overriding the equals operator to make sure we are comparing values on positions correctly
    def __eq__(self, obj):
        if self.x == obj.x and self.y == obj.y:
            return True
        else:
            return False



    