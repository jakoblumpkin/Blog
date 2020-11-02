from django.db import models

# Create your models here.
class thumbs(models.Model):
    like=models.IntegerField(blank=True)
    dislike=models.IntegerField(blank=True)


class section(models.Model):
    name = models.CharField(max_length=50)
    comment=models.TextField()
    time=models.CharField(max_length=50)
