from profiles.models import Profile, Gender
from avatar.models import Gravatar
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def edit_profile(request, id):
	p = Profile.objects.get(member=id)
	if request.method == "POST":
		if request.POST.get('age'):
			p.age = request.POST.get('age')
		if request.POST.get('gender'):
			p.gender = Gender.objects.get(id=request.POST.get('gender'))
		if request.POST.get('location'):
			p.location = request.POST.get('location')
		if request.POST.get('about'):
			p.about = request.POST.get('about')
		if request.POST.get('signature'):
			p.signature = request.POST.get('signature')
		p.save()
		return HttpResponseRedirect('/view_profile/'+str(p.member.id)+'/')
	context = {
		"p": Profile.objects.all(),
		"m": p,
		"g": Gender.objects.all(),
		"as": Gravatar.objects.all(), 
	}
	return render(request, 'profiles/edit_profile.html', context)


def view_profile(request, id):
	p = Profile.objects.get(member=id)
	context = {
		"p": Profile.objects.all(),
		"m": p,
		"g": Gender.objects.all(),
		"user": request.user,
		"as": Gravatar.objects.all()
	}
	return render(request, 'profiles/view_profile.html', context)
