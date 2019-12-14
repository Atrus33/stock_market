# Check the stock price! :moneybag: 

In this repository you can find a file named ```main.py``` that queries the FMP on-line service to receive the stock value of well-known companies in U.S. Dollars (but wait :warning: ... it's way more than this!).  
Some [parameters](#Command-line-parameters) are required to run the program but do not worry, everything is explained below!

If you run the program, executing the main file with: ```$ python main.py AAPL -u test -p test``` it will  give you results similar to the following: 

```
$ python main.py AAPL -u test -p test
Apple Inc. (Symbol: AAPL) has a stock value of 270.27 $.
```
> **Note:** the project requires the following modules to run: *argparse, sqlite3, random, hashlib, os, pandas, requests, json, unittest* and *sys*.

A user can choose, from a wide list, the **ticker** (company's stock symbol, **AAPL** in the example above) to analyse and the **currency** to express the stock price.  
**Authentication is required when runnnig the main file.**

[FMP](https://financialmodelingprep.com/) is an on-line resource that provides company valuation, **stock time series** (that we are using!) and stock market major indexes. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/).

 
> **Note:** More currencies and companies will be supported in the next release. :fire: 

## Documentation :notebook_with_decorative_cover:
Documentation can be found in: ```docs/_build/html/index.html``` and provides infos about the functions you can find in the various modules. Have a glimpse :eyeglasses:
 
To read them with your **default browser**, from the main folder use ```$ open docs/_build/html/index.html``` or, for other browsers you may have installed, follow these examples:
- **Chrome:** ```$ open -a "Google Chrome" docs/_build/html/index.html```
- **Safari:** ```$ open -a "Safari" docs/_build/html/index.html```


**DOCUMENTATION MADE WITH: [Sphinx](http://www.sphinx-doc.org/en/master/).**

## Data Files :open_file_folder:
Tickers and currencies data are stored in *.csv* files located in: ```stock_package/data/```.  There are 19 supported companies and 12 supported currencies in this **first release.**
#### Supported tickers (version 1.0):   

Ticker | Company
------------ | -------------  
AAPL | Apple Inc.  
MSFT | Microsoft Corporation 
FB | Facebook Inc.
ZNGA | Zynga Inc.
NVDA | NVIDIA Corporation
WBA | Walgreens Boots Alliance Inc.
GOOG | Alphabet Inc.
PIH | 1347 Property Insurance Holdings Inc.
BKNG | Booking Holdings Inc.
HIFS | Hingham Institution for Savings
Y | Alleghany Corporation
PTSI | P.A.M Transportation Services
CABO | Cable One Inc.
ROP | Roper Technologies Inc.
BLUE | Bluebird Bio Inc.
GHC | Graham Holdings Company
EQIX | Equinix Inc.
MLAB | Mesa Laboratories Inc.
MELI | MarcadoLibre Inc.

#### Supported currencies (version 1.0):
Currency | Currency to Dollar | Symbol
-------- | ------------------ | ------
euro | 0.9 | €
gbp | 0.77 | £
dollar | 1 | $
bitcoin | 0.00014 | BTC
aud | 1.47 | A$
rupee | 70.8 | ₹
bitcoincash | 0.0049 | BCH
hkdollar | 7.82 | HK$
litecoin | 0.023 | LTC
kwacha | 14.63 | ZK
riyal | 3.75 | SR
ruble | 63.55 | P

## Command line parameters :computer:
As we have mentioned in the first section, some command line parameters are required in order to run the main script.
#### Positional arguments
- **symbol**: The ticker (or stock) symbol associated with stocks of a company. **Only one** symbol can be passed.
> **Note:** You can access tickers (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_companies.csv```.

. 
#### Optional arguments
- **-h, --help:** show this help message and exit.  
- **-v:** Be more verbose. Some modules also include verbosity. There is **one level** of verbosity in this first release.   
- **-c:** The *currency* in which the value is expressed (**default: dollar**). If another currency is chosen, the **exchange rate** for that currency is applied.  
   > **Note:** You can access currencies (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_currencies.csv```.
- **-u U [required]:** the username (requires *-p*).  
- **-p P [required]:** the user's password.   
- **--version:** show program's version number and exit.

## How to populate the database :busts_in_silhouette:
In order to run ```main.py``` you will need a **username** and a **password**. The package comes with a **default user** with the following credenentials:
- *username*: **test**
- *password*: **test**

You may want to remove or add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allows you to populate the database.
> **Note:** adding and removing a user at the same time will be **denied** and no actions will be performed on the database.

#### Adding a new user
Use the parameter ```-add```. Requires the following:
 - **-u:** username 
 - **-p:** password
 ```
$ python dbmanager.py -add -u francesco_totti -p thecaptain_10 
Successfully inserted user francesco_totti
```
#### Removing a user
Use the parameter ```-rm```. Requires the following:
 - **-u:** username 
```
$ python dbmanager.py -rm -u francesco_totti
Successfully removed user francesco_totti
```
## Testing :name_badge:
Tests on parts of the code are provided here: ```stock_package/tests/``` .  
You can find 2 modules: ```test_csv_reader.py``` and ```test_currency_handler.py```.  
To run them **from the main folder** use:```python3 -m unittest -v -b stock_package/tests/test_MODULENAME.py```:

```
python3 -m unittest -v -b stock_package/tests/test_csv_reader.py
test_empty_datafie (test_csv_reader.TestCSVReader) ... ok
test_file_is_not_csv (test_csv_reader.TestCSVReader) ... ok
test_no_datafile (test_csv_reader.TestCSVReader) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

## Support
You need help? Get in touch with the authors on [Linkedin](https://www.linkedin.com/)!

## Authors and acknowledgment
Thank you all for the collaboration! Follow the authors on linkedin!
- [**Leonardo Antinucci**](https://www.linkedin.com/in/leonardo-antinucci-05b9b0125/)
- [**Federico Contini**](https://www.linkedin.com/in/federico-contini-457660162)
- [**Alexandru Catalin Duma**](https://www.linkedin.com/in/alexandru-duma/)
- [**Margherita Menegazzi**](https://www.linkedin.com/in/margherita-menegazzi-153b88199/)

Also thanks to [FMP](https://financialmodelingprep.com/) for the great service and comprehensive documentation!

## License
[MIT](https://choosealicense.com/licenses/mit/)