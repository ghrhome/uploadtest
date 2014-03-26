# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import RequestContext
import datetime

from forms import GalleryForm, PhotoForm, PhotoFormSet
from models import Gallery,Photos
def testurl(request):
	now=datetime.datetime.now()
	html="<h1> %s </h1>" %now
	return HttpResponse(html)


def galleryform(request):
	if request.method=="POST":
		form=GalleryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/ghrhome/galleries/")

	else:
		
		form=GalleryForm()

	return render_to_response("ghrhome/addgalleries.html",{'form':form,},RequestContext(request))


def galleries(request):
	try:
		galleries=Gallery.objects.all()
	except Exception :
		gallelries="wrong"
	return render(request, "ghrhome/galleries.html",{"galleries":galleries,})


def uploadPhoto(request):
	if request.method=="GET":
		gallery=request.GET["gallery"]
	if request.method=="POST":
		gallery=request.POST['gallery']
		form=PhotoForm(request.POST,request.FILES)
		if form.is_valid():

			# 这里处理得方法是根据已经提供gallery名称，进行gallery-查找--
			# gallery模型有问题，没有实现非重名gallery--需要修改
			
			#photo提交时要同时进行改名操作。
			gallery_id=Gallery.objects.filter(gallery_name=gallery)[0]
			photos=form.save(commit=False)
			photos.gallery=gallery_id
			photos.save()
			return HttpResponseRedirect("/ghrhome/photos/")
	else:
		form=PhotoForm()
	return render_to_response("ghrhome/uploadphoto.html",{'form':form,'gallery':gallery},RequestContext(request))


def photos(request):
	photos=Photos.objects.all()
	
	return HttpResponse(photos[2].photos.url)	
