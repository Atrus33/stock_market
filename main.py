from python_package import stock

n,price=stock.get_price("AAPL")
print("Company {} has a stock value of {}$".format(price, n))
n,price=stock.get_price("GOOGL")
print("Company {} has a stock value of {}$".format(price, n))


