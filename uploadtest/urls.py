#-*-coding=UTF-8-*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uploadtest.views.home', name='home'),
    # url(r'^uploadtest/', include('uploadtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^ghrhome/',include('ghrhome.urls')),
#	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

)

#开发服务器时，这里要映射到media设置才能正常显示图片
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$',"django.views.static.serve",{"document_root":settings.MEDIA_ROOT,}),

)
