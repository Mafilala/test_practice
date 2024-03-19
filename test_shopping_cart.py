import unittest
from product import Product  # Import the Product class
from shoppingCart import ShoppingCart  # Import the ShoppingCart class

class TestShoppingCart(unittest.TestCase):
    
    # Test the product to be added in an instace of Product

    # Test adding a product
    def test_addProduct(self):
        cart = ShoppingCart()
        product = Product("Shirt", 14.99, 1)
        cart.addProduct(product)
        self.assertEqual(len(cart.cart), 1)
        self.assertEqual(cart.cart[0], product)

    # Test getting the total with one product
    def test_getCartTotal_one_product(self):
        cart = ShoppingCart()
        product = Product("Hat", 29.95, 2)
        cart.addProduct(product)
        total = cart.getCartTotal()
        self.assertEqual(total, 59.90)

    # Test getting the total with multiple products
    def test_getCartTotal_multiple_products(self):
        cart = ShoppingCart()
        product1 = Product("Jeans", 39.99, 1)
        product2 = Product("Watch", 75.00, 1)
        cart.addProduct(product1)
        cart.addProduct(product2)
        total = cart.getCartTotal()
        self.assertEqual(total, 114.99)

    # Test getting the total with an empty cart
    def test_getCartTotal_empty_cart(self):
        cart = ShoppingCart()
        total = cart.getCartTotal()
        self.assertEqual(total, 0)

if __name__ == '__main__':
    unittest.main()
