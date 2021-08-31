import alpha_vantage
import requests
import os
import json
import following
import datetime

def auth():
    return os.environ.get("ALPHAVANTAGE_API")

def compile_text(set_tweets):
    alpha_API = auth()
    ticker_universe = alphavantage_list(alpha_API) # Find intersection of Tickers List & Tweets List
    compiled = set_tweets.intersect(ticker_universe)
    compiled= str(compiled).split().upper()
    return compiled

def alphavantage_list(ALPHAVANTAGE_API): # Takes the Alphavantage Key and returns a stripped, upper case set. Will be used to intersect with tweet text
    now = datetime.datetime.now().strftime("%y%m%d %H%M")
    ticker_universe_title = "SS Ticker Universe " + now + ".txt"
    ticker_universe_file = open(ticker_universe_title, 'w', encoding="utf-8") # Creates file with Ticker Universe contained
    ticker_universe = []

    CSV_URL = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={}".format(ALPHAVANTAGE_API)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        unprocessed_list = list(cr) # Returns list of all tickers in/active

    for row in unprocessed_list:  # Find all active tickers only
        state = row[6] # In/active state
        ticker = row[0] # Corresponding ticker in line
        if state == 'Active': # Screens out inactive tickers
            ticker_universe_file.write("{}, ".format(ticker))  # Save to the text file created above
            ticker_universe.append(ticker)  # active_list is list of active tickers

    ticker_universe = (', '.join(ticker_universe))
    ticker_universe = ticker_universe.split(", ")
    ticker_universe = set(ticker_universe)

    return ticker_universe



