from __future__ import unicode_literals
import random
from django.db import models

# Create your models here.
class CharManager(models.Manager):
    def randomizer(self, category=None):
        if category == None:
            category = random.randrange(1, 5)
        kanjiList = self.filter(p1=category)
        numberKanji = len(kanjiList)
        randomIndex = random.randrange(0, numberKanji)
        return kanjiList[randomIndex]

class Character(models.Model):
    kanji = models.CharField(max_length=50)
    skipcode  = models.CharField(max_length=50)
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)
    objects = CharManager()
