import datetime
from django.test import TestCase
from dashboard.utils import Utils


class UtilsTest(TestCase):

    def test_getStock(self):
        start_date = "2016-05-01"
        end_date = "2016-06-01"
        ticker = "INDEX_IBEX"

        data = Utils.getStockData(ticker, start_date, end_date)

        print("--data--")
        print(data)

        self.assertTrue(data.any)

    def test_getStocks(self):
        start_date = "2016-05-01"
        end_date = "2016-06-01"
        tickers = ["MC_SAN", "MC_BBVA", "MC_ITX", "MC_TEF", "MC_IBE", "INDEX_IBEX"]

        data = Utils.getDataForMultipleStocks(tickers, start_date, end_date)

        close_px = Utils.pivotTickersToColumns(data, "AdjClose")
        # peek at the result

        print(close_px)

        #daily_pc = close_px / close_px.shift(1) - 1

        #(precio  de cierre - precio de cierre día anterior) / (precio de  cierre día anterior)
        daily_pc = (close_px - close_px.shift(1) / close_px.shift(1))

        self.assertIsNotNone(self, daily_pc)


        print(daily_pc)

        values5 = daily_pc[3:10];
        sol = Utils.solveSystem(values5[[1, 2, 3, 4, 5]], values5[[0]])
        print(sol)
