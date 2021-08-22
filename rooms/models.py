from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Object Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"  # 이 메타클래스를 생성해주지 않으면 어드민페이지에서 amenitys라고 듬


class Facility(AbstractItem):

    """Facility Object Definition"""

    class Meta:
        verbose_name_plural = "Facility"


class HouseRule(AbstractItem):

    """HouseRule Object Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=90)
    file = models.ImageField(
        upload_to="room_photos"
    )  # 굿~!여기에 업로드 한 사진은 room_photos에 저장해줌!
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):  # 코어를 사용함으로써 타임스탬프모델 클래스를 다른 앱에서도 사용이 가능하다.

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        # 폴인키로 연결시켜 놓은 클래스에 related_name = users라고 해놓으면 user.rooms라는 것이
        # users모델에 생기는 것이 아니라 users가 참조하고 있는 rooms모델에 생긴다.
        # 따라서 참조해준 객체 입장에서 related_name을 설정해줘야 한다.
        # related_name을 쓰는 이유 django ORM 기능을 쓰기 위해(데이터베이스와의 연락) *정확히는 모름
        "users.User",
        related_name="rooms",
        on_delete=models.CASCADE,
        default=True,
    )  # cascade 삭제됬을시 유저와 관련된 모든 룸을 다같이 삭제함
    # 호스트가 유저이므로 서로 연결해줘야함 포린키
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )  # 한개의 방은 하나의 룸타임만 가질 수 있음
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name  # 이부분 복습할것! 어드민 페이지의 이름을 리턴값으로 바꿔줌!!

    def save(self, *args, **kwargs):
        # seoul을 입력했을때 첫글자만 대문자로 변환해 Seoul로 변환시켜 저장해줌. OOP와 관련되있음 ,학습필요
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):  # 와오 리뷰 평균 점수를 합한 평균
        all_reviews = self.reviews.all()  # ㄷ 리뷰 어드민에 related_name이 있는것 만으로 임포트가 됨
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round((all_ratings / len(all_reviews)), 2)
        return 0
