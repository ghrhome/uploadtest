from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from ghrhome.models import Gallery,Photos


PhotoFormSet=inlineformset_factory(Gallery,Photos)

class GalleryForm(ModelForm):
	class Meta:
		model=Gallery

class PhotoForm(ModelForm):
	class Meta:
		model=Photos

	
