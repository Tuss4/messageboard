from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category, SubCategory

def main(request):
	context = {
	"cats": Category.objects.all(),
	"scats": SubCategory.objects.all()
	}
	return render(request, "list.html", context)
