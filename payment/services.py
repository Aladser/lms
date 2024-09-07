import requests
import stripe
from stripe import Price

from config.settings import STRIPE_API_KEY


class StripeService:
    @staticmethod
    def create_price(amount, currency:str = 'usd') -> stripe.Price:
        """Создает цену в stripe"""

        stripe.api_key = STRIPE_API_KEY
        return stripe.Price.create(
            currency=currency,
            unit_amount=int(amount*100),
            product_data={"name": "Платеж"},
        )

    @staticmethod
    def convert_rub_to_usd(amount) -> float:
        """Конвертирует цены рубль -> доллар"""

        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        rate = data['Valute']['USD']['Value']

        return amount / rate

    @staticmethod
    def create_session(price: Price):
        """Создает stripe-сессию"""

        stripe.api_key = STRIPE_API_KEY
        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000/payment/success",
            line_items=[{"price": price.get('id'), "quantity": 1}],
            mode="payment",
        )
        return session.get('id'), session.get('url')

    @staticmethod
    def get_payment_status(payment):
        """Возвращает статус платежа"""

        stripe.api_key = STRIPE_API_KEY
        status = stripe.checkout.Session.retrieve(payment.session_id)
        return status
