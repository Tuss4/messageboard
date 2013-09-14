from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from structure.models import Category

def main(request):
	context = {
	"cats": Category.objects.all()
	}
	return render(request, "list.html", context)
