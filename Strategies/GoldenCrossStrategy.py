import math
import backtrader as bt


class GoldenCrossStrategy(bt.Strategy):

    params = (('fast', 7), ('slow', 21), ('order_percentage', 0.80), ('ticker', 'AAPL'))

    def log(self, txt, dt=None):

        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):

        self.size = 0
        self.dataclose = self.datas[0].close

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='7 day moving average'
         )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='21 day moving average'
        )

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        # print('next')
        self.log('Close, %.2f' % self.dataclose[0])

        if self.position.size == 0 and self.crossover > 0:

            amount_to_invest = (self.params.order_percentage * self.broker.cash)

            self.size = math.floor(amount_to_invest / self.data.close)

            print('BUY {} shares of {} at {}'.format(self.size, self.params.ticker, self.data.close[0]))

            self.buy(size=self.size)

        elif self.position.size > 0 > self.crossover:

            print('SELL {} shares of {} at {}'.format(self.size, self.params.ticker, self.data.close[0]))
            self.close()



