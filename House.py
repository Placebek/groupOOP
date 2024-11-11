#3
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls}, {self.doors}, {self.windows}, and a {self.roof}"

class HouseBuilder:
    def build_walls(self):
        pass

    def build_doors(self):
        pass

    def build_windows(self):
        pass

    def build_roof(self):
        pass

    def get_result(self):
        pass