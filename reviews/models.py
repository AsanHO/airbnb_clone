from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"  # 어드민페이지에서 이름이 바뀜!!

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)  # 소수점 두자리까지만 리턴함
