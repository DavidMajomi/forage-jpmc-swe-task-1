import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    
    for quote in quotes:
      # stock, bid_price, ask_price, price = getDataPoint(quote)
      expectedResults = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), ((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2))
      
      self.assertTupleEqual(getDataPoint(quote), expectedResults)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    
    for quote in quotes:
      # stock, bid_price, ask_price, price = getDataPoint(quote)
      expectedResults = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), ((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2))
      
      self.assertTupleEqual(getDataPoint(quote), expectedResults)

  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio_priceAGreaterThanPriceB(self):
    self.assertEquals(getRatio(10, 2), 5)

  def test_getRatio_priceALessThanPriceB(self):
    self.assertEquals(getRatio(2, 10), 0.2)

  def test_getRatio_priceAEqualsPriceB(self):
    self.assertEquals(getRatio(10, 10), 1)

  def test_getRatio_priceBEqualsZero(self):
    self.assertEquals(getRatio(10, 0), None)
    
if __name__ == '__main__':
    unittest.main()
