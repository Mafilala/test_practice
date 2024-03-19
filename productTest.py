import unittest
from product import Product  # Import the Product class
class TestProduct(unittest.TestCase):

    # Test the __init__ method
    def test_init(self):
        product = Product("Book", 19.99, 2)
        self.assertEqual(product.name, "Book")
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.quantity, 2)

    # Test the calculateTotal method
    def test_calculateTotal(self):
        product = Product("Pen", 5.50, 3)
        total = product.calculateTotal()
        self.assertEqual(total, 16.50)

        # Test with zero quantity
        product = Product("T-shirt", 25.00, 0)
        total = product.calculateTotal()
        self.assertEqual(total, 0)

    # Test with negative quantity
        product = Product("Laptop", 1299.99, -1)
        with self.assertRaises(ValueError):
            product.calculateTotal()

if __name__ == '__main__':
    unittest.main()
