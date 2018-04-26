from django.db import models

# Create your models here.
class Comment(models.Model):
    person_name = models.CharField(max_length=30)
    comment_content = models.TextField()