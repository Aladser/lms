from uu import Error

import stripe
from forex_python.converter import CurrencyRates
from stripe import Price

from config.settings import STRIPE_API_KEY


class StripeService:
    @staticmethod
    def create_price(amount, currency:str = 'usd') -> stripe.Price:
        """создает цену в stripe"""

        stripe.api_key = STRIPE_API_KEY
        return stripe.Price.create(
            currency=currency,
            unit_amount=int(amount*100),
            product_data={"name": "Платеж"},
        )

    @staticmethod
    def convert_rub_to_usd(amount) -> float:
        """конвертирует цену рубли -> доллары"""

        # заглушка
        c = CurrencyRates()
        try:
            rate = c.get_rates('USD')
            print(rate)
        except Exception as e:
            print(e)
        finally:
            return amount / 90

    @staticmethod
    def create_session(price: Price):
        """создает stripe-сессию"""

        stripe.api_key = STRIPE_API_KEY
        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000/payment/success",
            line_items=[{"price": price.get('id'), "quantity": 1}],
            mode="payment",
        )
        return session.get('id'), session.get('url')
