from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'story', 'date', 'media', 'tags']
		widgets = {
			'date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
		}

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']