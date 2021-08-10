from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():  # self.participants.all() 이 바로 queryset이다.
            usernames.append(user.username)
        return " , ".join(usernames)

    def count_messages(self):
        return self.messages.count()  # 메세지에서 포린키, relation_name했으므로 가능한 함수

    def count_participants(self):
        return self.participants.count()

    count_messages.short_description = "Number of messages"
    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"


# Create your models here.
