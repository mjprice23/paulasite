# Generated by Django 2.2.1 on 2019-05-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paulaapp', '0003_auto_20190523_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='claims_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='prospect_phone',
            field=models.CharField(max_length=12),
        ),
    ]
