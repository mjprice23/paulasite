# Generated by Django 2.2.1 on 2019-05-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paulaapp', '0008_auto_20190529_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='referral_source',
            field=models.CharField(max_length=50),
        ),
    ]
