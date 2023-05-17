from django import forms
from .models import Comments, Post

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'story', 'date_format', 'date', 'end_date_format', 'end_date', 'location', 'tags']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean_date(self):
        date_format = self.cleaned_data.get('date_format')
        date = self.cleaned_data.get('date')

        if date_format == '1':
            # Date format, no additional validation needed
            return date
        elif date_format == '2':
            # Month format, set the selected month as the date value
            month = self.cleaned_data.get('month')
            year = self.cleaned_data.get('year')
            return f'{year}-{month}-01'
        elif date_format == '3':
            # Year format, set the selected year as the date value
            year = self.cleaned_data.get('year')
            return f'{year}-01-01'
        elif date_format == '4':
            # Season format, set the selected season as the date value
            season = self.cleaned_data.get('season')
            return season

        return date




