# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Card(models.Model):
    card_number=models.CharField(max_length=30)
    card_cooperation=models.CharField(max_length=50)
    card_balance=models.FloatField()
    card_kind=models.CharField(max_length=20)
    card_date=models.DateField()

class Zhuanzhang(models.Model):
    zhuanzhang_date=models.DateField()
    zhuanzhang_source=models.CharField()
