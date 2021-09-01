# Twitter-Stock-Ticker-Compiler
This application extracts all stock tickers mentioned in your twitter feed.  The data is saved in a text file importable to Trading view. It does this using 2 methods 1. finds all tickers with '$' prefix and 2. compares all text in tweets to an active tickers list extracted from alphavantage.  
Currently, the application: 
1. Creates a text file which includes all tickers with a '$' prefix and 
2. Prints the number of times a stock ticker is mentioned &amp; which users mentioned it. 
3. Saves an output file "ZZZ Watchlist {date hour}"

Output is a file that is ready to upload to TradingView. It creates a list with 2 subheadings
1. "Most Mentioned" - which includes all tickers with 3 or more mentions
2. "Others" - which includes all tickers that were not $ prefixed and not mentioned more than 2 times. 
