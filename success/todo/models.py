from django.db import models

class TaskList(models.Model):
    # Model fields and methods
    ...
    
    class Meta:
        app_label = 'todo'
