from django.core.management.base import BaseCommand, CommandError
from structure.models import Topic, Post


class Command(BaseCommand):
	help = 'Sync categories with posts.'

	def handle(self, *args, **options):
		for p in Post.objects.all():
			p.cat = p.topic.parent
			p.save()
		self.stdout.write('Success')
