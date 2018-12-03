# Generated by Django 2.1.2 on 2018-12-03 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examenes', '0002_auto_20181202_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(upload_to='img/examenes/')),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField()),
                ('expediente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]