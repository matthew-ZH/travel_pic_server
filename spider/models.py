from django.db import models


# Create your models here.

class Photo(models.Model):

    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ('created',)
