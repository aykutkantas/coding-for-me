from django import forms
from .models import Comments, Post
#from django_google_maps import widgets as map_widgets
#import json

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'story', 'start_date', 'end_date', 'location', 'media', 'tags']
		widgets = {
			'start_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
			'end_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
			#'location': map_widgets.GoogleMapsAddressWidget(attrs={
			#	'data-autocomplete-options': json.dumps({ 'types': ['geocode',
            #	'establishment'], 'componentRestrictions': {
             #               'country': 'us'
		      #          }
               #     })
               #})
	    }


class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']



#CUSTOM_MAP_SETTINGS = {
 #   "GooglePointFieldWidget": (
  #      ("zoom", 15),
   #     ("mapCenterLocation", [60.7177013, -22.6300491]),
   # ),
#}