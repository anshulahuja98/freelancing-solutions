from django.db.models import fields


class MoneyField(fields.DecimalField):

    def __init__(self, verbose_name=None, name=None, max_digits=8,
                 decimal_places=2, **kwargs):
        super().__init__(verbose_name, name, **kwargs)
        self.max_digits, self.decimal_places = max_digits, decimal_places
