from django.db.models import fields


class MoneyField(fields.DecimalField):

    def __init__(self, verbose_name=None, name=None, max_digits=8,
                 decimal_places=2, **kwargs):
        super().__init__(verbose_name, name, **kwargs)
        self.max_digits, self.decimal_places = max_digits, decimal_places


class RatingField(fields.IntegerField):

    def __init__(self, *args, **kwargs):
        RATINGS = (
            (0, 'NA'),
            (1, 'Very Poor'),
            (2, 'Poor'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Excellent'),
        )

        kwargs['choices'] = RATINGS

        super(RatingField, self).__init__(*args, **kwargs)
