# events/models.py
from django.db import models


class Event(models.Model):

    type = models.CharField(max_length=20)
    public = models.BooleanField()
    repo_id = models.IntegerField()
    actor_id = models.IntegerField()

    def __str__(self):
        return f"{self.type} - Event ID: {self.pk}"
