# Generated by Django 2.2.1 on 2019-06-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paulaapp', '0014_auto_20190601_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='date_most_recent_visit',
            field=models.DateField(default=None),
        ),
    ]
