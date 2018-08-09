from django.core.exceptions import ValidationError


def validate_email(value):
    if '.edu' in value:
        raise ValidationError('We do not accept edu applications')


CATEGORIES = ['Asian', 'Mexican', 'Italian', 'Indian']


def validate_category(value):
    if value not in CATEGORIES:
        raise ValidationError('Not a valid category')