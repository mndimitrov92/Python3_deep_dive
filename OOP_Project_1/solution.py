#!/usr/bin/env python3
from datetime import datetime
from itertools import count
import numbers
from collections import namedtuple


Confirmation = namedtuple("Confirmation", "account_number transaction_type transaction_id date_utc")


class Account:
    """
    Class representing bank account functionality and attributes.  
    """
    INTEREST_RATE = 0.05
    TRANSACTION_ID = count(1000)
    WITHDRAW = 'W'
    DEPOSIT = 'D'
    INTEREST = 'I'
    DECLINED = 'X'

    def __init__(self, account_number, first_name, last_name, balance=0):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance

    @staticmethod
    def _validate_name(name, output_str):
        if not (name and isinstance(name, str) and name.strip()):
            raise ValueError(f"Provide a valid {output_str}")
        return name.strip()

    @classmethod
    def get_interest_rate(cls):
        return cls.INTEREST_RATE

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError("Interest rate must be a real number.")
        if value < 0:
            raise ValueError("Interest rate must be a positive number.")
        cls.INTEREST_RATE = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_name):
        self._first_name = Account._validate_name(new_name, "First Name")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_name):
        self._last_name = Account._validate_name(new_name, "Last Name")

    @property
    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if (self.balance + amount) < 0:
            raise ValueError("Balance cannot be <0 !")
        self._balance = amount

    def deposit(self, amount):
        """
        Deposits <amount> money into the account.
        """
        self.balance += amount
        print("Deposited {0}. Balance is now {1}.".format(amount, self.balance))
        confirmation_code = self._generate_confirmation_code(Account.DEPOSIT)
        return confirmation_code

    def withdraw(self, amount):
        """
        Withdraws <amount> money from the account.
        """
        if amount > self.balance:
            code = Account.DECLINED
        else:
            self.balance -= amount
            code = Account.WITHDRAW
            print("Withdrawn {0}. Balance is now {1}.".format(amount, self.balance))
        confirmation_code = self._generate_confirmation_code(code)
        return confirmation_code

    def pay_interest(self):
        self.balance += self.balance*Account.INTEREST_RATE
        print("Paying interest, balance is now: {0}.".format(self.balance))
        confirmation_code = self._generate_confirmation_code(Account.INTEREST)
        return confirmation_code

    @staticmethod
    def parse_confirmation_code(confirmation_code):
        """
        Parses the given confirmation code and separates in into chunks.
        """
        chunks = confirmation_code.split('-')
        transaction_type, account_number, raw_date, transaction_id = chunks
        try:
            date_utc = datetime.strptime(raw_date, "%Y%m%d_%H%M%S")
        except ValueError as ex:
            raise ValueError("Invalid transaction datetime") from ex
        return Confirmation(account_number, transaction_type, transaction_id, date_utc.isoformat())

    def _generate_confirmation_code(self, transaction_type):
        """
        Genearates and return a transaction code in the following format:
        [transaction_type]-[account>]-[date]-[transaction_id]
        """
        current_time = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        code = '-'.join([transaction_type, str(self._account_number), current_time, str(next(Account.TRANSACTION_ID))])
        return code

