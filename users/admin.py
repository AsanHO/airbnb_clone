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
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )  # 리스트 디스플레이를 하지 않으면 장고가 자기 마음대로 디스플레이를 한다. 그게 바로 UserAdmin.list_display
    # 이 리스트중에 우리가 커스텀한 것도, UserAdmin에 기본 탑재된 것들도 있다.
