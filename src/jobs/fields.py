from django.db.models import fields


class MoneyField(fields.DecimalField):
    """Custom MoneyField inherits from inbuilt DecimalField of django"""

    def __init__(self, verbose_name=None, name=None, max_digits=8, decimal_places=2, **kwargs):
        """Override constructor of DecimalField of django

        Limit max digits to 8 and decimal places to 2
        """

        super().__init__(verbose_name, name, **kwargs)
        self.max_digits, self.decimal_places = max_digits, decimal_places


class RatingField(fields.IntegerField):
    """Custom RatingField inherits from inbuilt IntegerField of django"""

    def __init__(self, *args, **kwargs):
        """Override constructor of IntegerField of django"""

        # Tuple of ratings presets
        RATINGS = (
            (0, 'NA'),
            (1, 'Very Poor'),
            (2, 'Poor'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Excellent'),
        )
        # Sends the RATINGS in the keyword arg of choices
        kwargs['choices'] = RATINGS
        super(RatingField, self).__init__(*args, **kwargs)
