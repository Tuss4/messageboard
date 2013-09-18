from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category, SubCategory, Topic, Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def view_cat(request, id):
	cat = Category.objects.get(id=id)
	context = {
		"user": request.user,
		"cat": cat,
		"scat": SubCategory.objects.filter(parent=id)
	}
	return render(request, "view_cat.html", context)


def view_subcat(request, id):
	sub = SubCategory.objects.get(id=id)
	context = {
		"user": request.user,
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
		"user": request.user,
		"sub": sub
	}
	return render(request, "topics/add_topic.html", context)


def view_topic(request, id):
	author = Topic.objects.get(id=id).author
	count = int(Topic.objects.filter(author=author).count()) + int(Post.objects.filter(author=author).count())
	member = ""
	u_count = ""
	if request.user.is_authenticated:
		member = User.objects.get(username=request.user.username)
		u_count = int(Topic.objects.filter(author=member).count()) + int(Post.objects.filter(author=member).count())
	u = False
	if request.user == Topic.objects.get(id=id).author or request.user.is_superuser():
		u = True
	topic_posts = Post.objects.filter(topic=id)
	posts = Paginator(topic_posts, 10)

	page = request.GET.get('page')
	try:
		post_list = posts.page(page)
	except PageNotAnInteger:
		post_list = posts.page(1)
	except EmptyPage:
		post_list = posts.page(paginator.num_pages)
	spec_page = int(topic_posts.count())/10
	p = Post()
	if request.method == "POST":
		p.post = request.POST.get('reply')
		p.title = "Re: " + Topic.objects.get(id=id).title
		p.date = datetime.datetime.now()
		p.author = User.objects.get(username=request.user.username)
		p.topic = Topic.objects.get(id=id)
		p.save()
		return HttpResponseRedirect('/topic/'+str(p.topic.id)+'/?page='+str(spec_page+1)+'#'+str(p.id))
	context = {
		"user": request.user,
		"posts": post_list,
		"u": u,
		"c": count,
		"mc": u_count,
		"t": Topic.objects.get(id=id)
	}
	return render(request, "topics/view_topic.html", context)


def edit_topic(request, id):
	t = Topic.objects.get(id=id)
	if request.method == "POST":
		t.title = request.POST.get('title')
		t.message = request.POST.get('message')
		t.description = request.POST.get('message')[0:40] + '...'
		t.save()
		return HttpResponseRedirect("/topic/"+id)
	context = {
		"user": request.user,
		"t": t
	}
	return render(request, "topics/edit_topic.html", context)


#Post views
def edit_post(request, id):
	p = Post.objects.get(id=id)
	if request.method == "POST":
		p.post = request.POST.get('message')
		p.save
		return HttpResponseRedirect('/topic/'+str(p.topic.id)+'/#'+str(p.id))
	context = {
		"user": request.user,
		"p": p
	}
	return render(request, 'posts/edit_post.html', context)
