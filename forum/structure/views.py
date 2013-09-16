from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category, SubCategory, Topic, Post
from django.contrib.auth.models import User
import datetime


def view_cat(request, id):
	cat = Category.objects.get(id=id)
	context = {
		"cat": cat,
		"scat": SubCategory.objects.filter(parent=id)
	}
	return render(request, "view_cat.html", context)


def view_subcat(request, id):
	sub = SubCategory.objects.get(id=id)
	context = {
		"sub": sub,
		"topics": Topic.objects.filter(parent=id),
		"u": request.user.is_authenticated()
	}
	return render(request, "list_sub.html", context)


#Topic Views
def add_topic(request, id):
	sub = SubCategory.objects.get(id=id)
	t = Topic()
	if request.method == "POST":
		t.title = request.POST.get('title')
		t.message = request.POST.get('message')
		t.description = request.POST.get('message')[0:40] + '...'
		t.author = User.objects.get(username=request.user.username)
		t.date = datetime.datetime.now()
		t.parent = sub
		t.save()
		return HttpResponseRedirect("/topic/"+str(t.id))
	context = {
		"sub": sub
	}
	return render(request, "topics/add_topic.html", context)


def view_topic(request, id):
	count = int(Topic.objects.filter(author=request.user).count()) + int(Post.objects.filter(author=request.user).count())
	u = False
	if request.user == Topic.objects.get(id=id).author or request.user.is_superuser():
		u = True
	context = {
		"u": u,
		"p": count,
		"t": Topic.objects.get(id=id)
	}
	return render(request, "topics/view_topic.html", context)


def edit_topic(request, id):
	t = Topic.objects.get(id=id)
	if request.method == "POST":
		t.title = request.POST.get('title')
		t.message = request.POST.get('message')
		t.save()
		return HttpResponseRedirect("/topic/"+id)
	context = {
		"t": t
	}
	return render(request, "topics/edit_topic.html", context)


#Post views
def new_post(request, id):
	return HttpResponse("Raagh!")
