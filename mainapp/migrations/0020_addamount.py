# Generated by Django 4.2.3 on 2023-08-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_regmodel_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='addamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
