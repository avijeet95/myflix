from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Search(models.Model):
	name = models.CharField(max_length=200,blank=False,null=False)
	year = models.IntegerField()
	def __unicode__(self):
		return self.name