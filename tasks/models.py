from django.db import models
import uuid

class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)


    def __str__(self):
        return self.title