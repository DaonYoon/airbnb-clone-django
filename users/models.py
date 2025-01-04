from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "FEMALE")

    class LanguageChoices(models.TextChoices):
        EN = ("en", "English")
        KR = ("ko", "Korean")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean WON"
        USD = "usd", "Dollor"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.EN,
    )
    currency = models.CharField(
        max_length=10,
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.WON,
    )
