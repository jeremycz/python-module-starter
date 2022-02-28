import unittest

from module.functions import add


class TestModuleFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
