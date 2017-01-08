# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class menu(models.Model):
  
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Nutrition = models.CharField(max_length=200)
    Price = models.IntegerField(default=170)
class specialmenu(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Nutrition = models.CharField(max_length=200)
    Price = models.IntegerField(default=170)
class survey(models.Model):
    question = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
class choice(models.Model):
    question = models.ForeignKey(survey, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    