from money import Money


class Bank:
    def __init__(self):
        self.exchange_rates = {}

    def add_exchange_rate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchange_rates[key] = rate

    def convert(self, money, currency):
        if money.currency == currency:
            return Money(money.amount, currency)

        key = money.currency + "->" + currency
        if key in self.exchange_rates:
            return Money(money.amount   * self.exchange_rates[key], currency)

        raise Exception(key)
