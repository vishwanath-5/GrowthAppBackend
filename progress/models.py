from django.db import models
from users.models import User

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)