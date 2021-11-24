from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    owner = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='%(class)s_requests_assigned', on_delete=models.CASCADE)
    
class Meta:
    verbose_name = 'Time'
    verbose_name_plural = 'Times'
    ordering =['id']

def __str__(self):
    return self.name