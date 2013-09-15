from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["id"]


class SubCategory(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	parent = models.ForeignKey(Category)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["id"]


class Topic(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	parent = models.ForeignKey(SubCategory)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["id"]


class Post(models.Model):
	title = models.CharField(max_length=50)
	post = models.TextField()
	date = models.DateTimeField()
	author = models.ForeignKey(User)
	topic = models.ForeignKey(Topic)

	def __unicode__(self):
		return unicode(self.title)
