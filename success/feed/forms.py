from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'story', 'date', 'location', 'media', 'tags']
		widgets = {
			'date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
		}
	
class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']



CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocation", [60.7177013, -22.6300491]),
    ),
}