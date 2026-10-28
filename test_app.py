
import unittest
from app import add, place_order, process_order

class UnitTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            place_order(0, 2)

class IntegrationTests(unittest.TestCase):
    def test_order_calculation(self):
        self.assertEqual(place_order(100, 2), 200)

    def test_payment(self):
        result = process_order(100, 2, True)
        self.assertEqual(result["status"], "success")

class SystemTests(unittest.TestCase):
    def test_complete_order(self):
        result = process_order(250, 2, True)
        self.assertEqual(result["total"], 500)
        self.assertEqual(result["status"], "success")

if __name__ == "__main__":
    unittest.main()
