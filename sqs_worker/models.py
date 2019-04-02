from django.db import models

class Todo(models.Model):
    label = models.CharField(max_length=255)