"""
A tool to explore the Collatz conjecture
Created by Daniel Tompkins tompkinsguitar@gmail.com
"""


class Collatz():
    def __init__(self, n, count_limit=1e100):
        self.n = n
        self.count_limit = count_limit
        self.sequence = []
        self.final_number = None
        self.count = 0
        self.valid = None

    def compute(self):
        while self.n not in self.sequence:
            self.count += 1
            self.sequence.append(self.n)
            self.final_number = self.n
            if self.count > self.count_limit:
                print(self.n, 'exceeded count limit of', self.count_limit)
                break
            if (self.n % 2) == 1:
                self.n = self.n * 3 + 1
            else:
                self.n = self.n // 2
        if self.final_number == 1:
            self.valid = True
        else:
            self.valid = False
