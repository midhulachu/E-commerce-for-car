# Generated by Django 4.2.3 on 2023-08-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_carstockmodel_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='carstockmodel',
            name='imagee',
            field=models.FileField(default=1, upload_to='mainapp/static'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carstockmodel',
            name='imageee',
            field=models.FileField(default=1, upload_to='mainapp/static'),
            preserve_default=False,
        ),
    ]
