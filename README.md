# Twitter-Stock-Ticker-Compiler
This application extracts all stock tickers mentioned in your twitter feed.  The data is saved in a text file importable to Trading view. It does this using 2 methods 1. finds all tickers with '$' prefix and 2. compares all text in tweets to an active tickers list extracted from alphavantage.  
Currently, the application: 
1. Creates a text file which includes all tickers with a '$' prefix (method 1 mentioned above only, but not method 2) 
2. 2. saves a full list of active tickers. 3. prints the number of times a stock ticker is mentioned &amp; which users mentioned it. 
