import unittest
from typing import Tuple

MAX_POWER = 20

def tilt_to_wheel_power(tilt: float) -> Tuple[int, int]:

    def power(tilt: float) -> int:
        power_reduction = MAX_POWER * tilt
        return int(MAX_POWER - power_reduction)

    left_tilt  = -min(tilt, 0)
    right_tilt = max(tilt, 0)
    left_power  = power(left_tilt)
    right_power = power(right_tilt)
    return left_power, right_power

for n in range(-10, 11, 2):
    tilt = n / 10.0
    print(tilt, tilt_to_wheel_power(tilt))

f = tilt_to_wheel_power

class Test(unittest.TestCase):

    def test_straight(self):
        self.assertEqual(f(0), (MAX_POWER, MAX_POWER))

    def test_half_left(self):
        self.assertEqual(f(-0.5), (MAX_POWER / 2, MAX_POWER))

    def test_left(self):
        self.assertEqual(f(-1), (0, MAX_POWER))

    def test_half_right(self):
        self.assertEqual(f(0.5), (MAX_POWER, MAX_POWER / 2))

    def test_right(self):
        self.assertEqual(f(1), (MAX_POWER, 0))
