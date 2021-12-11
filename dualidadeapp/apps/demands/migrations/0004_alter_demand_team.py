# Generated by Django 3.2.5 on 2021-12-11 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20211207_0122'),
        ('demands', '0003_auto_20211211_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]