# Generated by Django 2.2.5 on 2019-09-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.DeleteModel(
            name='Counter',
        ),
    ]
