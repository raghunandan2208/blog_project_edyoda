# Generated by Django 2.2.6 on 2020-04-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200415_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
