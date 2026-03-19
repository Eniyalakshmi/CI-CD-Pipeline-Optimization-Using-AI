import unittest
from app import calculate_sum

class TestApp(unittest.TestCase):

    def test_sum(self):
        data = [1,2,3,4]
        result = calculate_sum(data)
        self.assertEqual(result,10)

if __name__ == "__main__":
    unittest.main()
