import unittest
import random

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

class TestSquareFunctions(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_numbers(self):
        """Тест площади с положительными числами"""
        self.assertEqual(area(5), 25)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(10), 100)

    def test_area_zero(self):
        """Тест площади с нулевым значением"""
        self.assertEqual(area(0), 0)

    def test_area_float_numbers(self):
        """Тест площади с дробными числами"""
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(area(3.2), 10.24)
        self.assertAlmostEqual(area(0.5), 0.25)

    def test_area_random_positive_integers(self):
        """Тест площади со случайными положительными целыми числами"""
        for _ in range(100):  # 100 случайных тестов
            a = random.randint(1, 1000)
            expected = a * a
            self.assertEqual(area(a), expected)

    # Тесты для функции perimeter
    def test_perimeter_positive_numbers(self):
        """Тест периметра с положительными числами"""
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_zero(self):
        """Тест периметра с нулевым значением"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_numbers(self):
        """Тест периметра с дробными числами"""
        self.assertAlmostEqual(perimeter(2.5), 10.0)
        self.assertAlmostEqual(perimeter(3.2), 12.8)
        self.assertAlmostEqual(perimeter(0.5), 2.0)

    def test_perimeter_random_positive_integers(self):
        """Тест периметра со случайными положительными целыми числами"""
        for _ in range(100):
            a = random.randint(1, 1000)
            expected = 4 * a
            self.assertEqual(perimeter(a), expected)

if __name__ == '__main__':
    unittest.main()