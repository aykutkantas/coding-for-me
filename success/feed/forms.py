from django import forms
from .models import Comments, Post

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'story', 'start_date_format', 'start_date', 'end_date_format', 'end_date', 'location', 'tags']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }