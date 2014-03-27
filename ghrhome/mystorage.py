#-*-coding:UTF-8-*-
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings
import os,time,random
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
		
		
		
