from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Enables headless mode so that no browser window
# actually opens, speeding up the program.
options = Options()
options.add_argument('--headless')


ticker = input("Enter a stock ticker: ")
ticker = ticker.upper()
PJS_check = input("Use PhantomJS? (y or n): ")


def priceLookup(ticker):
    # Opens up the yahoo finance page for a given 
    # stock ticker and returns the current price.
    # Takes over 30 seconds to fetch data. PhantomJS
    # takes literally 1/10 of the time.

    driver = webdriver.Firefox(options=options)
    driver.get("https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch")
    price_locator = driver.find_element_by_css_selector('.Fz\(36px\)')
    price = price_locator.text
    driver.close()
    return price


###### DEPRECATED ######

# This actually runs significantly faster, but it
# is not recommended since selenium support for 
# PhantomJS is deprecated. Not sure which to use.
# Average runtime < 4 seconds. Very quick.

def priceLookupPJS(ticker):
    # Opens up the yahoo finance page for a given 
    # stock ticker and returns the current price.
    # Uses PhantomJS to not open up an actual browser.

    driver = webdriver.PhantomJS()
    driver.get("https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch")
    price_locator = driver.find_element_by_css_selector('.Fz\(36px\)')
    price = price_locator.text
    driver.close()
    return price


if PJS_check == 'y':
    print("The current price of " + ticker + " is: " + str(priceLookupPJS(ticker)))
else:
    print("The current price of " + ticker + " is: " + str(priceLookup(ticker)))