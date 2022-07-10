from Day4.task_1.сircle import sq_per_cir
import math
pi = math.pi

def test_sq_per_cir():
    assert sq_per_cir(5) == (70, 30)

def test_sq_per_cir1():
    assert sq_per_cir(10) == (80, 300)