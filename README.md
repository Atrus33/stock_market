# Check the stock price!

In this repository you can find a file named ```main.py``` that queries the FMP on-line service to receive the stock value of well-known companies in U.S. Dollars. 

If you run the program, executing the main file with: ```python main.py AAPL -u test -p test``` it will  give you results similar to the following: 

```
$ python main.py AAPL -u test -p test
Apple Inc. (Symbol: AAPL) has a stock value of 270.27 $.
```

[FMP](https://financialmodelingprep.com/) is an on-line resource that provides stock data. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/).

## Command line parameters
#### Positional arguments
- **symbol**: The ticker (or stock) symbol associated with stocks of a company. You can access them (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_companies.csv```
. 
#### Optional arguments
- **-h, --help:** show this help message and exit.  
- **-v:** Be more verbose.  
- **-c:** The *currency* in which the value is expressed. You can access them (and add more! :heavy_plus_sign: ) here: ```stock_package/data/allowed_currencies.csv```. 
- **-u U:** add a username name (requires *-p*).  
- **-p P:** the username password.   
- **--version:** show program's version number and exit.
## How to populate the database
In order to run ```main.py``` you will need a **username** and a **password**. The package comes with a default user with the following credenentials:
- *username*: **test**
- *password*: **test**

You may want to remove or add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allow you to populate the database.

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
To run them go in **stock_package/tests/** and use:```python -m unittest -v -b test_MODULENAME.py```:

```
$ python -m unittest -v -b test_csv_reader.py
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