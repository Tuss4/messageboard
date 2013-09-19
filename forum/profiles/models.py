from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	member = models.OneToOneField(User)
	age = models.CharField(max_length=2, null=True, blank=True)
	gender = models.ForeignKey('Gender', null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	about = models.TextField(null=True, blank=True)
	signature = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return unicode("%s - %s/%s/%s" %(self.member, self.age, self.gender, self.location))

	class Meta:
		ordering = ['member']


class Gender(models.Model):
	sexe = models.CharField(max_length=140)

	def __unicode__(self):
		return unicode(self.sexe)
