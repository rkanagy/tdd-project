import unittest

from portfolio import Portfolio
from money import Money
from bank import Bank


class TestMoney(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.add_exchange_rate("EUR", "USD", 1.2)
        self.bank.add_exchange_rate("USD", "KRW", 1100)

    def testMultiplication(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = Money(20, "EUR")
        self.assertEqual(twenty_euros, ten_euros.times(2))

    def testDivision(self):
        original_money = Money(4002, "KRW")
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(expected_money_after_division, original_money.divide(4))

    def testAddition(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        fifteen_dollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteen_dollars, portfolio.evaluate(self.bank, "USD"))

    def testAdditionOfDollarsAndEuros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate(self.bank, "USD")
        self.assertEqual(expected_value, actual_value, "%s != %s" % (expected_value, actual_value))

    def testAdditionOfDollarsAndWons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate(self.bank, "KRW")
        self.assertEqual(expected_value, actual_value, "%s != %s" % (expected_value, actual_value))

    def testAdditionWithMultipleMissingExchangeRates(self):
        one_dollar = Money(1, "USD")
        one_euro = Money(1, "EUR")
        one_won = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(
                Exception,
                "Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]"):
            portfolio.evaluate(self.bank, "Kalganid")

    def testConversion(self):
        bank = Bank()
        bank.add_exchange_rate("EUR", "USD", 1.2)
        tenEuros = Money(10, "EUR")
        self.assertEqual(bank.convert(tenEuros, "USD"), Money(12, "USD"))

    def testConversionWithMissingExchangeRate(self):
        bank = Bank()
        tenEuros = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            bank.convert(tenEuros, "Kalganid")


if __name__ == '__main__':
    unittest.main()
