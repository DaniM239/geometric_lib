import unittest
import random
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class TestCircleFunctions(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_numbers(self):
        """Тест площади с положительными числами"""
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)
        self.assertAlmostEqual(area(5), 25 * math.pi)

    def test_area_zero(self):
        """Тест площади с нулевым значением"""
        self.assertEqual(area(0), 0)

    def test_area_float_numbers(self):
        """Тест площади с дробными числами"""
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5)
        self.assertAlmostEqual(area(0.5), math.pi * 0.5 * 0.5)
        self.assertAlmostEqual(area(1.1), math.pi * 1.1 * 1.1)

    def test_area_random_positive_integers(self):
        """Тест площади со случайными положительными целыми числами"""
        for _ in range(100):  # 100 случайных тестов
            r = random.randint(1, 1000)
            expected = math.pi * r * r
            self.assertAlmostEqual(area(r), expected)

    # Тесты для функции perimeter
    def test_perimeter_positive_numbers(self):
        """Тест длины окружности с положительными числами"""
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test_perimeter_zero(self):
        """Тест длины окружности с нулевым значением"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_numbers(self):
        """Тест длины окружности с дробными числами"""
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)
        self.assertAlmostEqual(perimeter(0.5), math.pi)
        self.assertAlmostEqual(perimeter(1.1), 2.2 * math.pi)

    def test_perimeter_random_positive_integers(self):
        """Тест длины окружности со случайными положительными целыми числами"""
        for _ in range(100):
            r = random.randint(1, 1000)
            expected = 2 * math.pi * r
            self.assertAlmostEqual(perimeter(r), expected)

if __name__ == '__main__':
    unittest.main()