from django.db.models import fields


# Custom RatingField inherits from inbuilt DecimalField of django
class MoneyField(fields.DecimalField):
    # Override constructor of DecimalField of django
    def __init__(self, verbose_name=None, name=None, max_digits=8,
                 decimal_places=2, **kwargs):  # Fix max digits to 8 and decimal places to 2
        # Call constructor of the super class - DecimalField
        super().__init__(verbose_name, name, **kwargs)
        # Set default max digits and decimal_places
        self.max_digits, self.decimal_places = max_digits, decimal_places


# Custom RatingField inherits from inbuilt IntegerField of django
class RatingField(fields.IntegerField):
    # Override constructor of IntegerField of django
    def __init__(self, *args, **kwargs):
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
        # Call constructor of the super class - IntegerField
        super(RatingField, self).__init__(*args, **kwargs)
