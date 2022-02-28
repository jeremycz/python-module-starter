import unittest

from module.submodule.functions import subtract


class TestModuleFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(subtract(1, 2), -1)


if __name__ == "__main__":
    unittest.main()
