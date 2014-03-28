from django.db import models
from mystorage import MyStorage
# Create your models here.
fs=MyStorage()

class Gallery(models.Model):
	gallery_name=models.CharField(max_length=100)
	author=models.CharField(max_length=30)
	description=models.TextField()
	createDate=models.DateField(auto_now_add=True)	
	

class Photos(models.Model):
	photos_name=models.CharField(max_length=100)
	photos=models.ImageField(upload_to="./media/",storage=fs)
	gallery=models.ForeignKey(Gallery)




