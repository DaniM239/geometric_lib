import unittest
import random

def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

class TestTriangleFunctions(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_numbers(self):
        """Тест площади с положительными числами"""
        self.assertEqual(area(6, 4), 12)
        self.assertEqual(area(5, 3), 7.5)
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(3, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_float_numbers(self):
        """Тест площади с дробными числами"""
        self.assertAlmostEqual(area(2.5, 4), 5.0)
        self.assertAlmostEqual(area(3.2, 1.5), 2.4)
        self.assertAlmostEqual(area(0.5, 0.5), 0.125)

    def test_area_random_positive_integers(self):
        """Тест площади со случайными положительными целыми числами"""
        for _ in range(100):  # 100 случайных тестов
            a = random.randint(1, 1000)
            h = random.randint(1, 1000)
            expected = a * h / 2
            self.assertEqual(area(a, h), expected)

    # Тесты для функции perimeter
    def test_perimeter_positive_numbers(self):
        """Тест периметра с положительными числами"""
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(2, 7, 6), 15)

    def test_perimeter_zero(self):
        """Тест периметра с нулевыми значениями"""
        self.assertEqual(perimeter(0, 5, 3), 8)
        self.assertEqual(perimeter(3, 0, 4), 7)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float_numbers(self):
        """Тест периметра с дробными числами"""
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.0), 10.0)
        self.assertAlmostEqual(perimeter(1.2, 2.3, 3.4), 6.9)
        self.assertAlmostEqual(perimeter(0.5, 0.5, 0.5), 1.5)

    def test_perimeter_random_positive_integers(self):
        """Тест периметра со случайными положительными целыми числами"""
        for _ in range(100):
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            c = random.randint(1, 1000)
            expected = a + b + c
            self.assertEqual(perimeter(a, b, c), expected)

if __name__ == '__main__':
    unittest.main()
