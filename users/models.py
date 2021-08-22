from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # 이미 로그인 기능이 있다.
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

    avatar = models.ImageField(
        blank=True, upload_to="avatar"
    )  # 굿~!여기에 업로드 한 사진은 avatar에 저장해줌!
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=3, blank=True, default=LANGUAGE_KOR
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
