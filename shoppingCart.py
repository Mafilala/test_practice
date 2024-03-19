class ShoppingCart:
  def __init__(self) -> None:
    self.cart = []
  
  def addProduct(self, product):
    self.cart.append(product)

  def getCartTotal(self):
    total = 0
    for product in self.cart:
      total += product.calculateTotal()
    return total