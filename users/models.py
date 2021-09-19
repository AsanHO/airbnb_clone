import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string  # load templates and render
from core import managers as core_managers


class User(AbstractUser):  # 이미 로그인 기능이 있다.
    """Custom User Model"""

    """GENDER CHOICES"""
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    # 선언
    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )  # (a,b) a는 데이터 베이스, b는 form값에 반영된다.

    """LANGUAGE CHOICES"""
    LANGUAGE_ENG = "en"
    LANGUAGE_KOR = "kr"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, _("English")),
        (LANGUAGE_KOR, _("Korean")),
    )

    """CURRENCY CHOICES"""
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    """LOGIN CHOICES"""
    LOGIN_EMAIL = "Email"
    LOGIN_GITHUB = "Github"
    LOGIN_KAKAO = "Kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(
        blank=True, upload_to="avatar"
    )  # 굿~!여기에 업로드 한 사진은 avatar에 저장해줌!
    gender = models.CharField(
        _("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(_("bio"), blank=True)
    birthday = models.DateField(null=True)
    language = models.CharField(
        _("language"),
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
        default=LANGUAGE_KOR,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
        default=CURRENCY_KRW,
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50,
        choices=LOGIN_CHOICES,
        default=LOGIN_EMAIL,
    )
    objects = core_managers.CustomModelManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]  # 길이가 20인 랜덤문자열 만들기
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(  # https://docs.djangoproject.com/en/3.2/topics/email/
                _("Verify Airbnb Account"),
                strip_tags(html_message),  # html에서 텍스트만 추출
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
