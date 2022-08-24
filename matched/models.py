from django.db import models

class Match(models.Model):
    bname=models.CharField('B name', max_length=75, default='', blank=True)
    gname=models.CharField('G name', max_length=75, default='', blank=True)
