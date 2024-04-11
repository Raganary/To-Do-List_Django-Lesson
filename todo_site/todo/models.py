from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django import forms
 
 
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.title
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"