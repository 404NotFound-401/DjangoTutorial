# Generated by Django 2.2.5 on 2019-09-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchTest', '0002_auto_20190908_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]