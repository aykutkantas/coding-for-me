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
    def clean(self):
        cleaned_data = super().clean()
        date_format = cleaned_data.get('date_format')

        if date_format == '2':
            season = cleaned_data.get('season')
            year = cleaned_data.get('year')
            if season and year:
                cleaned_data['date'] = f"{year} {season}"
        elif date_format == '3':
            decade = cleaned_data.get('year')
            if decade:
                cleaned_data['date'] = f"{decade}s"

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        date_format = self.cleaned_data.get('date_format')

        if date_format == '2':
            season = self.cleaned_data.get('season')
            year = self.cleaned_data.get('year')
            if season and year:
                instance.date = f"{year} {season}"
        elif date_format == '3':
            decade = self.cleaned_data.get('year')
            if decade:
                instance.date = f"{decade}s"

        if commit:
            instance.save()

        return instance