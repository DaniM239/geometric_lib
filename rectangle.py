import unittest
import random

def area(a, b):
    return a * b


def perimeter(a, b):
    return 2 * (a + b)


class TestRectangleFunctions(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_numbers(self):
        """Тест площади с положительными числами"""
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(2, 7), 14)
        self.assertEqual(area(10, 10), 100)

    def test_area_zero(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(3, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_float_numbers(self):
        """Тест площади с дробными числами"""
        self.assertAlmostEqual(area(2.5, 4), 10.0)
        self.assertAlmostEqual(area(3.2, 1.5), 4.8)
        self.assertAlmostEqual(area(0.5, 0.5), 0.25)

    def test_area_random_positive_integers(self):
        """Тест площади со случайными положительными целыми числами"""
        for _ in range(100):  # 100 случайных тестов
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            expected = a * b
            self.assertEqual(area(a, b), expected)

    # Тесты для функции perimeter
    def test_perimeter_positive_numbers(self):
        """Тест периметра с положительными числами"""
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(2, 7), 18)
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_zero(self):
        """Тест периметра с нулевыми значениями"""
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(3, 0), 6)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_float_numbers(self):
        """Тест периметра с дробными числами"""
        self.assertAlmostEqual(perimeter(2.5, 4), 13.0)
        self.assertAlmostEqual(perimeter(3.2, 1.5), 9.4)
        self.assertAlmostEqual(perimeter(0.5, 0.5), 2.0)

    def test_perimeter_random_positive_integers(self):
        """Тест периметра со случайными положительными целыми числами"""
        for _ in range(100):
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            expected = 2 * (a + b)
            self.assertEqual(perimeter(a, b), expected)

if __name__ == '__main__':
    unittest.main()

