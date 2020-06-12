from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.user", related_name="Conversations", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    """"Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="Messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="Messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
