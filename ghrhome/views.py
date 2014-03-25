# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
import datetime

from forms import GalleryForm, PhotoForm, PhotoFormSet
from models import Gallery,Photos
def testurl(request):
	now=datetime.datetime.now()
	html="<h1> %s </h1>" %now
	return HttpResponse(html)


def galleryform(request):
	if request.method=="GET":
		form=GalleryForm(request.GET)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("galleries")

	else:
		
		form=GalleryForm()

	return render(request, "ghrhome/index.html",{'form':form,})


def galleries(request):
	try:
		galleries=Gallery.objects.all()
	except Exception :
		gallelries="wrong"
	return render(request, "ghrhome/galleries.html",{"galleries":galleries,})


	
