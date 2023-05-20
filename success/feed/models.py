from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from places.fields import PlacesField
from ckeditor.fields import RichTextField
from django.db.models import F, Q, When


# This model is for any post that a user posts on the website.
class Post(models.Model):
	title = models.CharField(max_length=255)
	story = RichTextField()
	CHOICE = (
		('1', 'Exact Date'), 
		('2', 'Season'),
		('3', 'Decade') 
	)
	date_format=models.CharField(choices=CHOICE, default=1)
	date= models.CharField(max_length=50, blank=True)
	end_date_format=models.CharField(blank=True, choices=CHOICE)
	end_date = models.DateField(blank=True)
	location = PlacesField()
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)
	

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
	
 
# Comment model links a comment with the post and the user. 
class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)

# It stores the like info. It has the user who created the like and the post on which like was made.
class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)








