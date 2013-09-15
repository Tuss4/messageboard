from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category, SubCategory, Topic


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
		"topics": Topic.objects.filter(parent=id)
	}
	return render(request, "list_sub.html", context)
