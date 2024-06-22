# tests/domain/test_equation.py
import pytest
from src.domain.models.equation import Equation

def test_solve_equation():
    equation = Equation(2, -4)  # Representa la ecuación 2x - 4 = 0
    assert equation.solve() == 2  # 2x = 4 -> x = 2
