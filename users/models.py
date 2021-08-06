from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    # 선언
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )  # (a,b) a는 데이터 베이스, b는 form값에 반영된다.

    LANGUAGE_ENG = "en"
    LANGUAGE_KOR = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENG, "english"), (LANGUAGE_KOR, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "usd"), (CURRENCY_KRW, "krw"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="")
    date = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=3, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    suprehost = models.BooleanField(default=False)
