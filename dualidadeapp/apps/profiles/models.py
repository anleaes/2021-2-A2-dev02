from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField('Tipo', max_length=50)
    photo = models.ImageField('Foto', upload_to='photos')
    phone = models.CharField('Celular', max_length=50)
    area = models.CharField('Area', max_length=50)
    biography = models.TextField('Biografia', max_length=300)
    git = models.CharField('Git', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering =['id']

    def __str__(self):
        return self.name