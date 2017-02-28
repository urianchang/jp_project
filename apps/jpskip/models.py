from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Character(models.Model):
    kanji = models.CharField(max_length=50)
    skipcode  = models.CharField(max_length=50)
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)
