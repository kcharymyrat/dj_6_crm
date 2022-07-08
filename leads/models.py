from statistics import mode
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"


class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
