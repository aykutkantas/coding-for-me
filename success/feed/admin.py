from django.contrib import admin
from .models import Post, Comments, Like
#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields
#import json

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
