# Generated by Django 2.1.2 on 2018-12-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0002_auto_20181127_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='conyugue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('C', 'Casado/a'), ('D', 'Divorciado/a'), ('S', 'Soltero/a'), ('V', 'Viudo/a')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='madre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='padre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
