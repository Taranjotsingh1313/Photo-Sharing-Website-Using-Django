from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class photos(models.Model):
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)