from django.core.management.base import BaseCommand, CommandError
from profiles.models import Profile 
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = 'Sync profiles to members'

	def handle(self, *args, **options):
		for u in User.objects.all():
			p = Profile()
			p.member = u
			p.save()

			self.stdout.write('Profiles synced!')
