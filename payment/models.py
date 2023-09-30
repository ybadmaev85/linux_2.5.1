from django.db import models

from users.models import User


class Pay(models.Model):
    PAY_CARD = 'card'
    PAY_CASH = 'cash'

    PAY_TYPES = (
        (PAY_CASH, 'наличные'),
        (PAY_CARD, 'перевод')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payday = models.PositiveSmallIntegerField(verbose_name='дата оплаты')
    is_paid = models.BooleanField(default=True, verbose_name='оплачено')
    summa = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(choices=PAY_TYPES, default=PAY_CASH, max_length=10,
                                verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.is_paid}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
