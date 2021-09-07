from yahoo_fin import stock_info as si


class Portfolio:
    def __init__(self, portfolio):
        """
        Initialize a portfolio object. It needs a dictionary with tickers as keys, and
        quantities as values.

        :param portfolio: dictionary
        """
        self.__portfolio = portfolio

    def __str__(self):
        portfolio_string = ''
        for stock in self.__portfolio:
            portfolio_string += stock + ' - ' + str(self.__portfolio[stock]) + '\n'

        return portfolio_string

    @property
    def portfolio(self):
        return self.__portfolio

    @property
    def portfolio_length(self):
        return len(self.__portfolio)

    def portfolio_size(self):
        # Dictionary for prices; key is the ticker
        live_prices = {}

        # Stores the portfolio size
        total = 0

        for stock in self.__portfolio:
            # Gets the live price using Yahoo Finance
            live_prices[stock] = si.get_live_price(stock)

            # Calculates the total amount
            total += self.__portfolio[stock] * live_prices[stock]

        return total

