# Generated by Django 3.2.5 on 2021-12-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20211207_0122'),
        ('demands', '0002_alter_demand_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='status',
            field=models.CharField(blank=True, choices=[('Disponível', 'Disponível'), ('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], default='Em andamento', max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.CreateModel(
            name='DemandTeamLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demands.demand')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'verbose_name': 'Like de time em demanda',
                'verbose_name_plural': 'Likes de time em demanda',
                'ordering': ['id'],
            },
        ),
    ]
