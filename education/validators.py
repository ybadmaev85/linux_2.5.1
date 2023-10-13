import re

from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get(self.field)
        youtube_pattern = r'^(https?://(?:www\.)?youtube\.com/)'

        if url:
            if not re.match(youtube_pattern, url):
                raise ValidationError(
                    'Недопустимый  URL. Разрешено только ссылки на Ютуб'
                )