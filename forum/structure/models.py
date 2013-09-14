from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["id"]
