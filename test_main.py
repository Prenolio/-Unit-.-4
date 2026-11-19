import unittest
from main import square


class SquareTestCase(unittest.TestCase):
    def test_square_from_1_to_9(self):
        expected = {
            1: 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49,
            8: 64,
            9: 81,
        }

        for a, result in expected.items():
            with self.subTest(a=a):
                self.assertEqual(square(a), result)


if __name__ == "__main__":
    unittest.main()