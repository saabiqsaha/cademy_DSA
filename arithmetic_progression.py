class ArithmeticProgression:
    def __init__(self, first = int, last = int, difference = int):
        self.first = first
        self.last = last
        self.difference = difference

    def set_first(self, first):
        self.first = first
    def set_last(self, last):
        self.last = last
    def set_difference(self, difference):
        self.difference = difference
    def get_first(self) -> int:
        return self.first
    def get_last(self) -> int:
        return self.last
    def get_difference(self) -> int:
        return self.difference
    def generator(self):
        sequence = []
        current = self.first
        while current <= self.last
    