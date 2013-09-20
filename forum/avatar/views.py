from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from avatar.models import Gravatar
from django.contrib.auth.models import User
import hashlib


def add_grav(request, id):
	g = Gravatar()
	if request.method == "POST":
		email = request.POST.get('email')
		url = 'http://www.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest()
		g.member = User.objects.get(id=id)
		g.gravatar = url
		g.save()
		return HttpResponse(url)
