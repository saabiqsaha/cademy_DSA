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
        if self.difference == 0:
            raise ValueError('difference cant be zero')
        sequence = []
        current = self.first
        while current <= self.last:
            sequence.append(current)
            current += self.difference
        return sequence
    def sum_sequence(self):
        if self.difference == 0:
            raise ValueError('Difference cant be zero')
        n = ((self.first + self.last) // self.difference) + 1
        return (n * (self.first + self.last)) // 2
    def __str__(self):
        return f"Arithmetic Progression: first= {self.first}, last={self.last}, and difference={self.difference}"
    

ap_test = ArithmeticProgression(first = 1, last = 12, difference = 5)
sequence = ap_test.generator()
print(ap_test)
print(sequence)