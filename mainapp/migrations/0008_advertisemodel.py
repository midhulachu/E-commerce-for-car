# Generated by Django 4.2.3 on 2023-08-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_cargalerymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertisemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='mainapp/static')),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
    ]
