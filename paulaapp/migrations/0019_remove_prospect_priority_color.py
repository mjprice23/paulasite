# Generated by Django 2.2.1 on 2019-06-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paulaapp', '0018_auto_20190602_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospect',
            name='priority_color',
        ),
    ]
