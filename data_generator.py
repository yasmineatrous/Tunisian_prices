import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class MarketDataGenerator:
    def __init__(self):
        self.vegetables = {
            'Tomatoes': (0.8, 2.5),
            'Potatoes': (1.2, 2.8),
            'Onions': (1.0, 2.2),
            'Carrots': (1.1, 2.4),
            'Peppers': (1.5, 3.5)
        }

        self.meat = {
            'Beef': (25.0, 35.0),
            'Lamb': (28.0, 38.0),
            'Chicken': (12.0, 18.0),
            'Turkey': (15.0, 22.0),
            'Fish': (20.0, 30.0)
        }

    def generate_price(self, min_price, max_price):
        return round(np.random.uniform(min_price, max_price), 2)

    def generate_daily_prices(self):
        prices = {'Category': [], 'Item': [], 'Price': [], 'Previous_Price': []}

        # Generate vegetable prices
        for item, (min_price, max_price) in self.vegetables.items():
            prices['Category'].append('Vegetables')
            prices['Item'].append(item)
            prices['Price'].append(self.generate_price(min_price, max_price))
            prices['Previous_Price'].append(self.generate_price(min_price, max_price))

        # Generate meat prices
        for item, (min_price, max_price) in self.meat.items():
            prices['Category'].append('Meat')
            prices['Item'].append(item)
            prices['Price'].append(self.generate_price(min_price, max_price))
            prices['Previous_Price'].append(self.generate_price(min_price, max_price))

        return pd.DataFrame(prices)