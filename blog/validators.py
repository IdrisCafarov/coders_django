from django.core.exceptions import ValidationError

def validate_title(value):
    if value == "hello":
        raise ValidationError(
            f"{value} is not correct"
        )