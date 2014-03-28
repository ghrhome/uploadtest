from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from ghrhome.models import Gallery,Photos


PhotoFormSet=inlineformset_factory(Gallery,Photos)

class TextWidget(forms.Textarea):
	class Media:
		css={}
		js=('/media/js/tinymce/tinymce.min.js','/media/js/textareas.js')

class GalleryForm(ModelForm):
#	description=forms.CharField(widget=forms.HiddenInput)
	class Meta:
		model=Gallery
		fields=["gallery_name","author","description"]
		widgets={"description":TextWidget(),}
class PhotoForm(ModelForm):
	class Meta:
		model=Photos
		fields= ["photos_name","photos"]

class UploadPhoto(forms.Form):
	upload_photo=forms.ImageField()

