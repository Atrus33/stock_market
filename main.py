from python_package import stock
import sys

if len(sys.argv) > 1:
    company = sys.argv[1]
    n,price=stock.get_price(company)
    print("Company {} has a stock value of {}$".format(price, n))

else:
    print("Tell me the company you want to know about!")
    exit()



