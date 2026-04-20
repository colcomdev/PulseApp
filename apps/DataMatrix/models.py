from django.db import models
from django.contrib.auth.models import User

class DataMatrix(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    FullName = models.CharField(max_length=100,default="IT E")
    UserNumber= models.PositiveIntegerField()
    Suspended = models.PositiveIntegerField()
    Description = models.TextField()
    Code= models.PositiveIntegerField()
    Action = models.TextField(max_length=50)
    Comment = models.TextField(max_length=100)
    Summary = models.TextField(max_length=50)

    def __str__(self):
        return self.UserNumber