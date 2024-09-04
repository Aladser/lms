from rest_framework import serializers
import re

class LinkValidator:
    """Проверка наличия ссылок на URL-ресурсы кроме ютуб"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        http_pattern = r'^http://+[a-zA-Z0-9._%+-]+\.+[a-zA-Z]{2,}$'
        https_pattern = r'^https://+[a-zA-Z0-9._%+-]+\.+[a-zA-Z]{2,}$'
        www_pattern = r'www\.+[A-Za-z0-9!-_.]+\.[a-zA-Z]{2,}'

        tmp_value = dict(value).get(self.field)
        formatted_value = str(tmp_value).replace('youtube.com', '')
        if re.search(https_pattern, formatted_value) or re.search(http_pattern, formatted_value) or re.search(www_pattern, formatted_value):
            raise serializers.ValidationError('существуют ссылки на другой URL-ресурс кроме ютуба')
