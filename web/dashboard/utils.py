import datetime
import pandas as pd
import pandas_datareader.data as web
import requests
import urllib.parse
import numpy as np


class Utils:
    # read data from Yahoo! Finance for a specific
    # stock specified by ticker and between the start and end dates
    def getStockData(ticker, start, end):

        url = "https://www.quandl.com/api/v3/datasets/YAHOO/" + ticker + ".csv?api_key=4TmMFx9HJ6sY4zcwHqc5&start_date=" + start + "&end_date=" + end
        # read the data
        data = pd.read_csv(filepath_or_buffer=url)
        # rename this column
        data.rename(columns={'Adj Close': 'AdjClose'}, inplace=True)
        data.rename(columns={'Adjusted Close': 'AdjClose'}, inplace=True)

        # insert in the ticker as a column
        data.insert(0, "Ticker", ticker)
        return data

    # gets data for multiple stocks
    # tickers: a list of stock symbols to fetch
    # start and end are the start and end dates
    def getDataForMultipleStocks(tickers, start, end):
        # we return a dictionary
        stocks = dict()
        # loop through all the tickers
        for ticker in tickers:
            # get the data for the specific ticker
            s = Utils.getStockData(ticker, start, end)
            # add it to the dictionary
            stocks[ticker] = s
        # return the dictionary
        return stocks

    # given the dictionary of data frames,
    # pivots a given column into values with column
    # names being the stock symbols
    def pivotTickersToColumns(raw, column):
        items = []
        # loop through all dictionary keys
        for key in raw:
            # get the data for the key
            data = raw[key]
            # extract just the column specified
            subset = data[["Date", "Ticker", column]]
            # add to items
            items.append(subset)
        # concatenate all the items
        combined = pd.concat(items)
        # reset the index
        ri = combined.reset_index()
        # return the pivot
        return ri.pivot("Date", "Ticker", column)

    def solveSystem(values, results):


        a = np.array(values[:4])
        b = np.array(results[:4])

        #append more ecuations 1+1+1+1+1 = 1
        newrowa=[1,1,1,1,1]
        a = np.vstack([a,newrowa])

        newrowb=[1]
        b=np.vstack([b,newrowb])

        print("--- A ---")
        print(a)
        print("--- B ---")
        print(b)

        x=np.linalg.solve(a,b)
        print("--- SOL ---")
        print(x)

        return x
