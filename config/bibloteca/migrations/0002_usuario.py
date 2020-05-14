# Generated by Django 3.0.6 on 2020-05-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibloteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=30)),
                ('ejemplares', models.ManyToManyField(to='bibloteca.Ejemplar')),
            ],
        ),
    ]