# src/domain/models/equation.py
class Equation:
    def __init__(self, a, b):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero.")
        self.a = a
        self.b = b

    def solve(self):
        return -self.b / self.a
