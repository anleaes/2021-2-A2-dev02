from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    owner = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through='UserTeam', blank=True)
    
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'
        ordering =['id']

    def __str__(self):
        return self.name


class UserTeam(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuário de Time'
        verbose_name_plural = 'Usuários de Time'
        ordering =['id']

    def __str__(self):
        return self.team.name