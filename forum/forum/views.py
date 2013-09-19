from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category, SubCategory, PostCount
from profiles.models import Profile
from django.contrib import auth
from django.contrib.auth.models import User


def main(request):
	context = {
	"p": Profile.objects.all(),
	"cats": Category.objects.all(),
	"scats": SubCategory.objects.all()
	}
	return render(request, "list.html", context)


def login(request):
	if request.method == "POST":
		user = request.POST.get('user')
		passw = request.POST.get('pass')
		user = auth.authenticate(username=user, password=passw)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			raise Http404()
	return render(request, 'auth/login.html')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	u = User()
	c = PostCount()
	p = Profile()
	if request.method == "POST":
		u.username = request.POST.get('user')
		u.set_password(request.POST.get('pass'))
		u.email = request.POST.get('email')
		u.is_active = True
		u.is_staff = False
		u.is_superuser = False
		u.save()
		c.user = u
		c.count = 0
		c.save()
		p.member = u
		p.save()
		return HttpResponseRedirect('/login/')
	return render(request, 'auth/register.html')
