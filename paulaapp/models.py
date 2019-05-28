from django.db import models

import uuid
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
import logging

from phonenumber_field.modelfields import PhoneNumberField

log = logging.getLogger(__name__)


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):    #inheriting fields from UUID and TimeStampedModel
    class Meta:
        abstract = True


class Prospect(TimeStampedUUIDModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prospect_email = models.EmailField(max_length=100)
    prospect_phone = models.CharField(max_length=12)  # opportunity to reformat this later
    #prospect_phone = PhoneNumberField()
    owns_property: bool = models.BooleanField(default=False)
    if owns_property:
        owns_UP: bool = models.BooleanField(default=False)
        if not owns_UP:
            property_location = models.CharField(max_length=200)
    buy_new_construction_only: bool = models.BooleanField(default=False)
    claims_agent: bool = models.BooleanField(default=False)

    class Meta:     #lets you define superficial things (.latest) used outside the database
        ordering = ['last_name', 'first_name', 'prospect_email', 'prospect_phone']


    def __str__(self):  #   when you print, what shows up
        return '{} {}'.format(self.first_name, self.last_name, self.prospect_email, self.prospect_phone)


class Document(TimeStampedUUIDModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
# Create your models here.
