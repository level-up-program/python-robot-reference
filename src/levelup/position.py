class Position ():

    x = -100
    y = -100

    def __init__(self, x: int, y: int):
         # TODO: implement method here and remove the print statement below
        print("Position constructor method not yet implemented")

    # Overriding the equals operator to make sure we are comparing values on positions correctly - prewritten for you
    def __eq__(self, obj):
        if self.x == obj.x and self.y == obj.y:
            return True
        else:
            return False



    