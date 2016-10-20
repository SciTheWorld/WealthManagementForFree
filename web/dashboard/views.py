from blaze.expr.reductions import count
from django.http import HttpResponse
from django.shortcuts import render

import datetime
import pandas as pd
import pandas_datareader.data as web
import requests
import urllib.parse


def index(request):
    # Create your views here.
    return render(request, "dashboard/index.html", {})


def static_sample(request):
    # Create your views here.
    return render(request, "dashboard/sample.html", {})


def tests(request):
    return render(request, "dashboard/allTogether.html")


def test_csv(request):
    # Create your views here.

    start_date = datetime.datetime(2011, 5, 1)
    end_date= datetime.datetime(2016, 6, 1)
    ticker = "INDEX_IBEX"


    # base_url = 'https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_IBEX.csv?'
    # df = pd.read_csv(filepath_or_buffer=base_url + urllib.parse.urlencode(params))


    df = pd.read_csv(
        filepath_or_buffer="https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_IBEX.csv?start_date=2011-05-01")

    # url = "http://" + request.get_host() + "/static/dashboard/tests/ibex2.csv"
    # df = pd.read_csv(filepath_or_buffer=url)


    return HttpResponse(
        df.to_csv(columns=["Date", "Open", "High", "Low", "Close", "Volume"], index=False, float_format='%.2f'))


