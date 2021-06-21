from datetime import date, datetime
from decimal import Decimal
import json
from pprint import pprint

import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
from marshmallow import fields, Schema, post_load


class Stock:
    def __init__(self, symbol, date, open_order, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open_order = open_order
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def toJSON(self):
        return {
                'objecttype': type(self).__name__,
                'symbol': self.symbol,
                'date': self.date,
                'open_order': self.open_order,
                'high': self.high,
                'low': self.low,
                'close': self.close,
                'volume': self.volume
            }


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.volume = volume
        self.commission = commission


    def toJSON(self):
        return {
                'objecttype': type(self).__name__,
                'symbol': self.symbol,
                'timestamp': self.timestamp,
                'order': self.order,
                'price': self.price,
                'commission': self.commission,
                'volume': self.volume
            }

# Example 
activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}


# Excercise 1 solution -> Serialize the data
class CustomJSONEncoder(json.JSONEncoder):

    def default(self, arg):
        if isinstance(arg, (date, datetime)):
            return arg.isoformat()
        elif isinstance(arg, (Stock, Trade)):
            return arg.toJSON()
        elif isinstance(arg, Decimal):
            return str(arg)
        else:
            super().default(arg)


# Excercise 2 solution -> Deserialize the data
class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, arg):
        data =json.loads(arg)
        return self.parse_data(data)

    def parse_data(self, data):
        if isinstance(data, dict):
            get_objecttype = data.get('objecttype', None)
            if get_objecttype == 'Stock':
                return self.handle_stock(data)
            elif get_objecttype == 'Trade':
                return self.handle_trade(data)
            else:
                if isinstance(data, dict):
                    for k,v in data.items():
                        data[k] = self.parse_data(v)
                return data
        elif isinstance(data, list):
            for index, item in enumerate(data):
                data[index] = self.parse_data(item)
        return data

    def handle_stock(self, stock_dict):
        return Stock(symbol=stock_dict['symbol'],
                     date=stock_dict['date'],
                     open_order=Decimal(stock_dict['open_order']),
                     high=Decimal(stock_dict['high']),
                     low=Decimal(stock_dict['low']),
                     close=Decimal(stock_dict['close']),
                     volume=int(stock_dict['volume']))

    def handle_trade(self, trade_dict):
        return Trade(
                symbol=trade_dict['symbol'],
                timestamp=trade_dict['timestamp'],
                order=trade_dict['order'],
                price=Decimal(trade_dict['price']),
                volume=int(trade_dict['volume']),
                commission=Decimal(trade_dict['commission'])
                )

# Excercise 3 solution -> Serialize and deserialize with Marshmallow
# Create the schemas first
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open_order = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Int()

    @post_load
    def make_stock(self, data, *args, **kwargs):
        return Stock(**data)


class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    volume = fields.Int()
    commission = fields.Decimal(as_string=True)

    @post_load
    def make_trade(self, data, *args, **kwargs):
        return Trade(**data)


class ActivitySchema(Schema):
    quotes = fields.Nested(StockSchema, many=True)
    trades = fields.Nested(TradeSchema, many=True)


if __name__ == '__main__':
    encoded = json.dumps(activity, cls=CustomJSONEncoder, indent=2) 
    print(encoded)
    print("===="*20)
    decoded = json.loads(encoded, cls=CustomJSONDecoder)
    pprint(decoded)
    print("===="*20)
    # The serialization
    activity_serialize = ActivitySchema().dumps(activity, indent=2)
    print(activity_serialize)
    # The deserailization
    activity_deserialize = ActivitySchema().loads(activity_serialize)
    pprint(activity_deserialize)


