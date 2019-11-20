from python_package import stock
import sys

 # get the label of the company
if len(sys.argv) > 1:
    company = sys.argv[1]
    n, price = stock.get_price(company)
    print("Company {} has a stock value of {}$".format(price, n))

 # if the user does not pass a label as an input
else:
    print("Tell me the company you want to know about!")
    exit()



