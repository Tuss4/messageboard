from django.db import models
from django.contrib.auth.models import User

class Gravatar(models.Model):
	member = models.OneToOneField(User)
	gravatar = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return unicode('%s - %s' %(self.member, self.gravatar))
