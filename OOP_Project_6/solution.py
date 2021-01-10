from datetime import datetime
from http import HTTPStatus
import json
import traceback

class WidgetException(Exception):
	"""
	Base exception class for the widget application. Provides base functionality foe the
	custom exception that are needed.
	"""
	msg = "Widget Error."
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR

	def __init__(self, *args, customer_msg=None):
		super().__init__(*args)
		self.customer_msg = customer_msg or self.msg
		if args:
			self.msg = args[0]

	def log(self):
		"""
		Log messages to the terminal in a formatted way
		"""
		to_be_logged = {
			"http_status": self.http_status.value,
			"type": type(self).__name__,
			"message": self.msg,
			"args": self.args[1:],
			"traceback": list(self.traceback)
		}
		result = f"Exception: {to_be_logged['type']} logged at {datetime.now().isoformat()}\n" \
				 f"Status code: {to_be_logged['http_status']}\n" \
			     f"Message: {to_be_logged['message']}\nArguments: {to_be_logged['args']} \n" \
			     f"Traceback: {to_be_logged['traceback']}"
		print(result)
		return result

	def to_json(self):
		"""
		Exports the exception information in a json format. 
		"""
		output = {
			"code": self.http_status.value,
			"message": f"{self.http_status.phrase} : {self.customer_msg}",
			"exception type": type(self).__name__,
		}
		return json.dumps(output)

	@property
	def traceback(self):
		"""
		Provide formatted exception traceback.
		"""
		# from exception method in the traceback class returns a generator
		return traceback.TracebackException.from_exception(self).format()


# Supplier Exceptions group
class SupplierException(WidgetException):
	msg = "Supplier Exception"


class NotManufacturedError(SupplierException):
	msg = "Not manufactured anymore"


class ProductionDelayedError(SupplierException):
	msg = "Production delayed"


class ShippingDelayedError(SupplierException):
	msg = "Shipping delayed"

# Checkout exxception group
class CheckoutException(WidgetException):
	msg = "Checkout Exception"


class InventoryTypeError(CheckoutException):
	msg = "Inventory type exception"


class OutOfStockError(InventoryTypeError):
	msg = "out of stock"


class PricingException(CheckoutException):
	msg = "Pricing exception"


class InvalidCouponCode(PricingException):
	msg = "invalid coupon code"
	http_status = HTTPStatus.BAD_REQUEST


class CouponStackError(PricingException):
	msg = "cannot stack coupons"
	http_status = HTTPStatus.BAD_REQUEST

