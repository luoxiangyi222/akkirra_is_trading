import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

import backtrader as bt
from FirstStrategy import TestStrategy


cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000000)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# ########################
AAPL_HISTORY = 'aapl.csv'


# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname=AAPL_HISTORY,
    # Do not pass values before this date
    # fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values after this date
    # todate=datetime.datetime(2000, 12, 31),
    reverse=False)


cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


cerebro.plot()