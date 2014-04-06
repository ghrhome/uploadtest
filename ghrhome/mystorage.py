#-*-coding:UTF-8-*-
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from django.utils import simplejson
import os,time,random
from django.http import HttpResponse
class MyStorage(FileSystemStorage):
	def __init__(self,location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL):
		super(MyStorage,self).__init__(location,base_url)

	def _save(self,name,content):
		#文件扩展名
		ext=os.path.splitext(name)[1]
		#文件目录名
		d=os.path.dirname(name)
		#定义文件名，年月日时秒+随机数
		fn=time.strftime("%Y%m%d%H%M%S")
		fn = fn+ "_%d" %random.randint(0,100)
		#合并文件名
		name=os.path.join(d,fn+ext)
#		name=fn+ext
		return super(MyStorage,self)._save(name,content)
		
		
def handle_upload_file(f):
	media_root=settings.MEDIA_ROOT
	media_url=settings.MEDIA_URL
	wrapped_file=UploadedFile(f)
	file_name=wrapped_file.name
	ext=os.path.splitext(file_name)[1]
	fn=time.strftime("%Y%m%d%H%M%S")
	fn=fn+ "_%d" %random.randint(0,100)
	new_file_name=fn+ext
	
	with open((media_root+new_file_name),"wb+") as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	result=[]
	result.append({"name":new_file_name,
			"url":media_url+new_file_name,})
	response_data=simplejson.dumps(result)
	return HttpResponse(response_data,mimetype="application/json")


def handle_upload_file2(f):
        media_root=settings.MEDIA_ROOT
        media_url=settings.MEDIA_URL
        wrapped_file=UploadedFile(f)
        file_name=wrapped_file.name
        ext=os.path.splitext(file_name)[1]
        fn=time.strftime("%Y%m%d%H%M%S")
        fn=fn+ "_%d" %random.randint(0,100)
        new_file_name=fn+ext

        with open((media_root+new_file_name),"wb+") as destination:
                for chunk in f.chunks():
                        destination.write(chunk)

        result=[]
        result.append({"name":new_file_name,
                        "url":media_url+new_file_name,})
        response_data=simplejson.dumps(result)
	print response_data
        return HttpResponse(response_data,mimetype="application/json")
			
