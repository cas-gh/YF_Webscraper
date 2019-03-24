# YF_Webscraper
Asks user for a stock ticker and returns the current price.

An interesting thing about this file, is it provides two different methods for
opening Firefox in headless mode. Strangely enough, the deprecated PhantomJS method
works like literally 10x faster than the recommended method. For this reasons, I
have included both in the file. A prompt when using the program asks the user if
they would like to use PhantomJS despite Selenium support for it being deprecated.
If someone could figure out why this happens, please let me know. I asked 
StackOverflow and, predictably, got no helpful responses.
