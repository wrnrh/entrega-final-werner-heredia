# Generated by Django 4.1.5 on 2023-02-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resenas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='5', max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='items')),
            ],
        ),
    ]