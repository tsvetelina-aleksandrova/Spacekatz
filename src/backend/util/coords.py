class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, attr, value):
        if isinstance(value, int):
            object.__setattr__(self, attr, value)
        else:
            raise ValueError("Coords should be ints")
