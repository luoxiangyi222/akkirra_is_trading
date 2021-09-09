import datetime  # For datetime objects

import backtrader as bt
from Strategies.FirstStrategy import TestStrategy
from Strategies.GoldenCrossStrategy import GoldenCrossStrategy


cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000000)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# ########################
AAPL_HISTORY = '/Users/akira/PycharmProjects/AkiraIsTrading/stocks_history_data/aapl.csv'


# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname=AAPL_HISTORY,
    # Do not pass values before this date
    fromdate=datetime.datetime(2021, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2021, 12, 31),
    reverse=False)

cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

cerebro.adddata(data)

cerebro.addstrategy(GoldenCrossStrategy)

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


cerebro.plot()