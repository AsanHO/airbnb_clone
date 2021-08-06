from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (  # 기본 제공 필드세트와 + 내가 만든 커스텀프로필 필드 세트
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "date",
                    "language",
                    "currency",
                    "suprehost",
                )
            },
        ),
    )
