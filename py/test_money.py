import unittest


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        self.assertEqual(ten_dollars, five_dollars.times(2))

    def testMultiplicationInEuros(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = Money(20, "EUR")
        self.assertEqual(twenty_euros, ten_euros.times(2))

    def testDivision(self):
        original_money = Money(4002, "KRW")
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(expected_money_after_division, original_money.divide(4))


if __name__ == '__main__':
    unittest.main()
