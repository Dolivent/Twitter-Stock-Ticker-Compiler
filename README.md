# Twitter-Stock-Ticker-Compiler

**General Info**
This application extracts all stock tickers mentioned in your twitter feed.  The data is saved in a text file importable to Trading view. It does this using 2 methods 1. finds all tickers with '$' prefix and 2. compares all text in tweets to an active tickers list extracted from alphavantage.  
Currently, the application: 
1. Creates a text file which includes all tickers with a '$' prefix and tickers without prefix by comparing all tweet text to a list of active tickers from AlphaVantage
2. Prints the number of times a stock ticker is mentioned &amp; which users mentioned it in the comand prompt. 
3. Saves an output file "ZZZ Watchlist {date hour}"

Output is a file that is ready to upload to TradingView. It creates a list with 2 subheadings
1. "Most Mentioned" - which includes all tickers with 3 or more mentions
2. "Others" - which includes all tickers that were not $ prefixed and not mentioned more than 2 times. 

**Requirements**
The directory must contain a file called ".env" with the following text:

    ALPHAVANTAGE_API = 62FVCU5OI06KTS # go to https://www.alphavantage.co/support/#api-key to apply
    BEARER_TOKEN = AAAAAAAAAAAAAAAAAAAAAOGUTAEAAAAAmQ9%2Brgtjkg7YLpPEQhKlahLu%2F64%3DPYmvZNS3ZOe5CLNQ2jfXow #go to https://apps.twitter.com/ to apply
    user_id = 136959900147386 #Twitter ID of user. Use https://tweeterid.com/ to find quickly

    #the above are dummies. replace with your own keys and target twitter IDs (of feed you would like to extract from)

**Contributors**
   - Forked from @xaviernadal https://github.com/xaviernadal/StockTickersSearch  (will add as a fork thingo on Github when I work out how to do that)
   - @[] helped with in depth revision of code as well as hands on logic and methogolody help and review as well as many hours of coaching and guidence [link]
   - @e0 comments guidence on logic and methodology as well as feedback on review https://github.com/e0 
