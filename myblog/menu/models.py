from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
    class Meta():
        db_table = 'menu'
    menu_title = models.CharField(max_length=20)
    menu_description = models.TextField()
    menu_url = models.CharField(max_length=200)
    menu_disabled = models.BooleanField(default=False)
