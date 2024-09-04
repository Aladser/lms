from rest_framework import serializers
import re

class LinkValidator:
    """Проверка наличия ссылок на URL-ресурсы кроме ютуб"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        formatted_value = str(tmp_value).replace('youtube.com', '')

        pattern = r'(?:https?://|www+\.)+[A-Za-z0-9!-_.]+\.+[a-zA-Z]{2,}'

        if re.search(pattern, formatted_value):
            raise serializers.ValidationError('существуют ссылки на другой URL-ресурс кроме ютуба')
