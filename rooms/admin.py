from django.contrib import admin
from django.utils.html import mark_safe  # 기본적으로 장고는 인풋을 막는다.(보안상) 그ㄱㄹ
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):  # 이함수의 용도, 어드민페이지에서 리스트를 추가해주는데 특별한 용도, 카운트같은
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):  # 포토 어드민페이지가 아닌 룸어드민페이지에서 사진CRUD를 가능하게 만들어줌

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (  # 중복되는 모델이 있으면 안된다!!
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    ordering = (
        "price",
        "bedrooms",
    )

    list_display = (
        "name",
        "host",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",  # 함수화
        "count_photos",  # 함수화 해야함
        "total_rating",
    )
    list_filter = (
        "host__superhost",  # 유저의 슈퍼호스트도 조회가능, 어째서 슈프레호스트에서 오탈자를 수정하면 오류가 생기는 것인지 의문.
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "instant_book",
        "city",
        "country",
    )

    raw_id_fields = ("host",)  # 유저가 많아지면 일반적인 셀렉터로 찾기어려움, 이건 검색형태로 바꿔줌

    search_fields = (
        "=city",
        "^host__username",
    )  # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenity Count"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Room Admin Definition"""  # 이거 해주는이유, 클래스가 방대해지고 협업이 필요할때

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
