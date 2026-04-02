import unittest
from tkinter import Tk
from billing import billClass

class TestBilling(unittest.TestCase):
    # https://docs.python.org/3/library/unittest.html
    # Gemini was used here a bit, mostly to help setup
    # the billClass with @classmethod
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.root.withdraw()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def setUp(self):
        self.app = billClass(self.root)
        self.app.cart_list = []

    # Unit tests

    def test_bill_calculation(self):
        """
        Make sure math is correct for bill amount and net pay
        with discount set to 10.
        """

        # Should be equal to 200, 100 * 2
        self.app.cart_list = [['1', 'test', '100', '2', '10']]
        self.app.var_discount.set("10")
        self.app.bill_update()
        self.assertEqual(self.app.bill_amnt, 200.0)
        self.assertEqual(self.app.net_pay, 180.0)

    def test_empty_cart_totals(self):
        """
        Make sure that with empty cart the bill amount and
        net pay are 0.
        """
        self.app.bill_update()
        self.assertEqual(self.app.bill_amnt, 0)
        self.assertEqual(self.app.net_pay, 0)

    def test_zero_discount(self):
        """
        Confirm zero discount functions, so amount = net.
        """
        self.app.cart_list = [['1', 'test', '100', '1', '10']]
        self.app.var_discount.set("0")
        self.app.bill_update()
        self.assertEqual(self.app.net_pay, 100.0)

    # Integration tests

    def test_add_to_cart_flow(self):
        """
        This tests selecting product, setting quantity,
        adding and then checking total.
        """
        self.app.var_pid.set("1")
        self.app.var_pname.set("test")
        self.app.var_price.set("50")
        self.app.var_qty.set("3")
        self.app.var_stock.set("10")

        # Simulate clicking add
        self.app.add_update_cart()

        self.assertEqual(len(self.app.cart_list), 1)
        self.assertEqual(self.app.bill_amnt, 150.0)

    def test_clear_all_flow(self):
        """
        This tests adding an item, setting customer, clearing all
        and then verifying that everything reset.
        """
        self.app.cart_list = [['1', 'test', '10', '1', '10']]
        self.app.var_cname.set("Customer")
        self.app.var_discount.set("20")

        # Simulate clicking clear all
        self.app.clear_all()

        self.assertEqual(len(self.app.cart_list), 0)
        self.assertEqual(self.app.var_cname.get(), "")
        self.assertEqual(self.app.bill_amnt, 0)
        self.assertEqual(self.app.var_discount.get(), "5")

    # Regression test

    def test_discount_updates_immediately(self):
        """
        Make sure that net changes when you type in a new discount
        """
        self.app.cart_list = [['1', 'test', '100', '1', '10']]
        self.app.var_discount.set("10")
        self.app.bill_update()
        self.assertEqual(self.app.net_pay, 90.0)

        # Simulate changing discount from 10 to 50
        self.app.var_discount.set("50")
        self.app.bill_update()
        self.assertEqual(self.app.net_pay, 50.0)

if __name__ == '__main__':
    unittest.main()
