import alpha_vantage
import requests
import os
import json
import following
import datetime
import csv
from dotenv import load_dotenv

def auth():
    load_dotenv()  # take environment variables from .env.
    return os.environ.get("ALPHAVANTAGE_API")

def unprefixed_tickers(set_tweets):
    alpha_API = auth()
    ticker_universe = alphavantage_list(alpha_API) # Find intersection of Tickers List & Tweets List
    unprefixed_tickers = set_tweets.intersection(ticker_universe)
    unprefixed_tickers = list(unprefixed_tickers)
    unprefixed_tickers = (', '.join(unprefixed_tickers))

    return unprefixed_tickers

def alphavantage_list(ALPHAVANTAGE_API): # Takes the Alphavantage Key and returns a stripped, upper case set. Will be used to intersect with tweet text

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
            ticker_universe.append(ticker)  # active_list is list of active tickers

    ticker_universe = (', '.join(ticker_universe))
    ticker_universe = ticker_universe.split(", ")
    ticker_universe = set(ticker_universe)

    return ticker_universe



