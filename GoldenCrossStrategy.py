import math
import backtrader as bt


class GoldenCrossStrategy(bt.strategies):
    def log(self, txt, dt=None):
        """
        Logging function for this strategy
        :param txt: historical data
        :param dt: time
        :return:
        """

        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None
        self.bar_executed = 0

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXECUTED {}'.format(order.executed.price))
            self.bar_executed = len(self)

        self.order = None

    def next(self):
        print('next')
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

