class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length


    # create get_area here
    def get_area(self):
        return round((3 * ((3 ** 0.5) * (self.side_length ** 2))) / 2, 3)
