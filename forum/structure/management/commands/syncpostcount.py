from django.core.management.base import BaseCommand, CommandError
from structure.models import Topic, Post, PostCount
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = 'Sync user topics and posts to count model.'

	def handle(self, *args, **options):
		for u in User.objects.all():
			x = PostCount()
			x.user = u
			x.count = int(Topic.objects.filter(author=u).count()) + int(Post.objects.filter(author=u).count())
			x.save()
