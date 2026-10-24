import unittest

from greeting import greet


class GreetTest(unittest.TestCase):
    def test_greets_with_hey(self):
        self.assertEqual(greet("world"), "Hey, world!")


if __name__ == "__main__":
    unittest.main()
