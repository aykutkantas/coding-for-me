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

def clean_start_date(self):
    start_date_format = self.cleaned_data.get('start_date_format')
    start_date = self.cleaned_data.get('start_date')

    if start_date_format == '1':
        # Date format, no additional validation needed
        return start_date
    elif start_date_format == '2':
        # Month format, set the selected month as the start_date value
        return start_date
    elif start_date_format == '3':
        # Year format, set the selected year as the start_date value
        return start_date
    elif start_date_format == '4':
        # Season format, set the selected season as the start_date value
        return start_date

    return start_date


