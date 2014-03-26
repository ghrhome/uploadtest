from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
	url(r'try/$',views.testurl,name="try"),
	url(r'galleryform/$',views.galleryform,name="galleryform"),
	url(r'galleries/$',views.galleries,name="galleries"),
	url(r'uploadphoto/$',views.uploadPhoto,name="uploadphoto"),
	url(r'photos/$',views.photos,name="photos"),
)
