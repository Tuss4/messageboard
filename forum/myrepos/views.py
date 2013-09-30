from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import urllib2, simplejson


def main(request):
	url = "https://api.github.com/users/Tuss4/repos?sort=updated"
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read() 
	rdata = simplejson.loads(data)
	rlist = []
	for r in rdata:
		rlist.append("<a href='"+r['html_url']+"'>"+r['name']+"</a>")
	context = {
		"rl": rlist
	}
	return render(request, "myrepos.html", context)
