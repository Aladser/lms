import requests
import stripe
from django.urls import reverse
from stripe import Price

from config.settings import STRIPE_API_KEY, SERVICE_ADDR


class StripeService:
    @staticmethod
    def create_price(product_name, amount, currency:str = 'usd') -> stripe.Price:
        """Создает цену в stripe"""

        stripe.api_key = STRIPE_API_KEY
        return stripe.Price.create(
            currency=currency,
            unit_amount=int(amount*100),
            product_data={"name": product_name},
        )

    @staticmethod
    def convert_rub_to_usd(amount) -> float:
        """Конвертирует цены рубль -> доллар"""

        api_addr = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = requests.get(api_addr).json()
        rate = data['Valute']['USD']['Value']

        return amount / rate

    @staticmethod
    def create_session(price: Price):
        """Создает stripe-сессию"""

        stripe.api_key = STRIPE_API_KEY
        session = stripe.checkout.Session.create(
            success_url=f"{SERVICE_ADDR}/{reverse('payment:success')}",
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
