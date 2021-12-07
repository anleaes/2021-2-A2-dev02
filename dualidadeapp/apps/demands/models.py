from django.db import models
from teams.models import Team
from django.contrib.auth.models import User

# Create your models here.
class Demand(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField('Titulo', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    deadline = models.DateField('Prazo Final', auto_now=False, auto_now_add=False) 
    type = models.CharField('Tipo', max_length=50)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    file = models.FileField('Documento', upload_to='docs')
    repository = models.CharField('Repositorio', max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
        ordering =['id']

    def __str__(self):
        return self.name