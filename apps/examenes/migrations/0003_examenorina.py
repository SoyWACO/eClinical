# Generated by Django 2.1.3 on 2018-11-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0002_examensangre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamenOrina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=10)),
                ('aspecto', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('ph', models.IntegerField(blank=True, null=True)),
                ('nitrito', models.CharField(blank=True, max_length=50, null=True)),
                ('proteinas', models.IntegerField(blank=True, null=True)),
                ('glucosa', models.IntegerField(blank=True, null=True)),
                ('cuerpo_cetonico', models.CharField(blank=True, max_length=50, null=True)),
                ('bilirubina', models.CharField(blank=True, max_length=50, null=True)),
                ('sangre_oculta', models.IntegerField(blank=True, null=True)),
                ('leucocitos', models.CharField(blank=True, max_length=50, null=True)),
                ('hematies', models.CharField(blank=True, max_length=50, null=True)),
                ('cel_epitelalias', models.CharField(blank=True, max_length=50, null=True)),
                ('cilindros', models.CharField(blank=True, max_length=50, null=True)),
                ('parasitos', models.CharField(blank=True, max_length=50, null=True)),
                ('otros', models.CharField(blank=True, max_length=50, null=True)),
                ('cristales', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]