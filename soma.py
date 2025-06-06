import unittest
from soma import soma

class TestSoma(unittest.TestCase):
    def test_soma_2_e_3(self):
        self.assertEqual(soma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
