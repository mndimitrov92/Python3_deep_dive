import unittest
import solution
from datetime import datetime
from http import HTTPStatus
import json




class TestGenericExceptionAttributes(unittest.TestCase):
	"""
	Tests the generic attributes of the exceptions.
	"""
	expected = (
			# Exception type, defualt_msg, error code, hierarchy position
			(solution.SupplierException, "Supplier Exception", HTTPStatus.INTERNAL_SERVER_ERROR, solution.WidgetException),
			(solution.NotManufacturedError, "Not manufactured anymore", HTTPStatus.INTERNAL_SERVER_ERROR, solution.SupplierException),
			(solution.ProductionDelayedError, "Production delayed", HTTPStatus.INTERNAL_SERVER_ERROR, solution.SupplierException),
			(solution.ShippingDelayedError, "Shipping delayed", HTTPStatus.INTERNAL_SERVER_ERROR, solution.SupplierException),
			(solution.CheckoutException, "Checkout Exception", HTTPStatus.INTERNAL_SERVER_ERROR, solution.WidgetException),
			(solution.InventoryTypeError, "Inventory type exception", HTTPStatus.INTERNAL_SERVER_ERROR, solution.CheckoutException),
			(solution.OutOfStockError, "out of stock", HTTPStatus.INTERNAL_SERVER_ERROR, solution.InventoryTypeError),
			(solution.PricingException, "Pricing exception", HTTPStatus.INTERNAL_SERVER_ERROR, solution.CheckoutException),
			(solution.InvalidCouponCode, "invalid coupon code", HTTPStatus.BAD_REQUEST, solution.PricingException),
			(solution.CouponStackError, "cannot stack coupons", HTTPStatus.BAD_REQUEST, solution.PricingException),
		)
	def test_generic(self):
		for exc, msg, code, parent in self.expected:
			with self.subTest(f"Testing {exc.__name__}:"):
				self.assertEqual(exc.http_status, code)
				self.assertTrue(issubclass(exc, parent))
				self.assertEqual(exc.msg, msg)


class TestWidgetException(unittest.TestCase):
	"""
	Test cases overing the generic withet exception functionality.
	"""

	def test_customer_message(self):
		ex = solution.WidgetException(customer_msg="Test message")
		self.assertEqual(ex.customer_msg, "Test message")

	def test_default_customer_message(self):
		ex = solution.WidgetException(10, 20)
		self.assertEqual(ex.customer_msg, "Widget Error.")

	def test_exception_argumets(self):
		ex = solution.WidgetException(10, 20, 30)
		self.assertEqual(ex.args, (10, 20, 30))
		self.assertEqual(ex.msg, 10)

	def test_exception_logging(self):
		ex = solution.WidgetException(10, 20, 30, customer_msg="My message")
		expected_line1 = "Exception: WidgetException logged at"
		expected_line2 = "Status code: 500"
		expected_line3 = "Message: 10\nArguments: (20, 30)"
		
		expected_line4 = "Traceback: ['solution.WidgetException: (10, 20, 30)\\n']"
		result = ex.log()
		self.assertIn(expected_line1, result)
		self.assertIn(expected_line2, result)
		self.assertIn(expected_line3, result)
		self.assertIn(expected_line4, result)

	def test_exception_logging_no_args(self):
		ex = solution.WidgetException(customer_msg="My message")
		expected_line1 = "Exception: WidgetException logged at"
		expected_line2 = "Status code: 500"
		expected_line3 =  "Message: Widget Error.\nArguments: ()"
		expected_line4 = "Traceback: ['solution.WidgetException\\n']"
		result = ex.log()
		self.assertIn(expected_line1, result)
		self.assertIn(expected_line2, result)
		self.assertIn(expected_line3, result)
		self.assertIn(expected_line4, result)

	def test_export_to_json(self):
		ex = solution.WidgetException()
		json_output = ex.to_json()
		expected = {'code': 500,
					'message': 'Internal Server Error : Widget Error.',
					'exception type': 'WidgetException'
					}
		self.assertEqual(json.loads(json_output), expected)


	def test_export_to_json_with_customer_msg(self):
		ex = solution.WidgetException(customer_msg="My message")
		json_output = ex.to_json()
		expected = {'code': 500,
					'message': 'Internal Server Error : My message',
					'exception type': 'WidgetException'
					}
		self.assertEqual(json.loads(json_output), expected)

	def test_traceback(self):
		ex = solution.WidgetException()
		self.assertEqual(list(ex.traceback), ['solution.WidgetException\n'])


if __name__ == '__main__':
	unittest.main()
