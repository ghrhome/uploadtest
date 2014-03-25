from django.db import models

# Create your models here.
class Gallery(models.Model):
	gallery_name=models.CharField(max_length=100)
	author=models.CharField(max_length=30)
	
	

class Photos(models.Model):
	photos_name=models.CharField(max_length=100)
	photos=models.ImageField(upload_to="./media/")
	gallery=models.ForeignKey(Gallery)




