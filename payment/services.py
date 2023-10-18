from education.models import Сourse, Lesson


def stripe_price_data(obj):
    return {
        'currency': 'usd',
        'unit_amount': obj.price,
        'product_data': {
            'name': obj.title,
        },
    }
