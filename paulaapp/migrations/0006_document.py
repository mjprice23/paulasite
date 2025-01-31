# Generated by Django 2.2.1 on 2019-05-23 21:10

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('paulaapp', '0005_auto_20190523_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('prospect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paulaapp.Prospect')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
