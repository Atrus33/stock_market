# Check the stock price! :moneybag: 

In this repository you can find a file named ```main.py``` that queries the FMP on-line service to receive the stock value of well-known companies in U.S. Dollars. 

If you run the program, executing the main file with: ```python main.py AAPL -u test -p test``` it will  give you results similar to the following: 

```
$ python main.py AAPL -u test -p test
Apple Inc. (Symbol: AAPL) has a stock value of 270.27 $.
```
> **Note:** the project requires the following modules to run: *argparse, sqlite3, random, hashlib, os, pandas, requests, json, unittest* and *sys*.

A user can choose, from a wide list, the **ticker** (company's stock symbol) to analyse and the **currency** to express the stock price.  
**Authentication is required.**

[FMP](https://financialmodelingprep.com/) is an on-line resource that provides stock data. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/).

 
> **Note:** More currencies and companies will be supported in the next release. :fire: 

## Documentation :notebook_with_decorative_cover:
Documentation can be found in: ```docs/_build/html/index.html```
Made with: [Sphinx](http://www.sphinx-doc.org/en/master/).

## Data Files :open_file_folder:
Tickers an currencies data are stored in *.csv* files located in: ```stock_package/data/```.  
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

## Command line parameters
#### Positional arguments
- **symbol**: The ticker (or stock) symbol associated with stocks of a company.
> **Note:** You can access them (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_companies.csv```.

. 
#### Optional arguments
- **-h, --help:** show this help message and exit.  
- **-v:** Be more verbose.  
- **-c [required]:** The *currency* in which the value is expressed (**default: dollar**).  
   > **Note:** You can access them (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_currencies.csv```.
- **-u U [required]:** add a username name (requires *-p*).  
- **-p P [required]:** the user password.   
- **--version:** show program's version number and exit.

## How to populate the database
In order to run ```main.py``` you will need a **username** and a **password**. The package comes with a **default user** with the following credenentials:
- *username*: **test**
- *password*: **test**

You may want to remove or add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allows you to populate the database.

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
## Testing
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

## License
[MIT](https://choosealicense.com/licenses/mit/)