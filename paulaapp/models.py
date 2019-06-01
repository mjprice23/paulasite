from django.db import models

import uuid
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
import logging
import datetime

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
    SUNDAY = 'SUN'
    SATURDAY = 'SAT'
    DAY_CHOICES = (
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday',)
    )
    RENT = 'R'
    OWN = 'O'
    UNKNOWN = 'U'
    LIVING_CHOICES = (
        (RENT, 'Renting'),
        (OWN, 'Own property'),
        (UNKNOWN, 'Unknown')
    )
    HIGH = 'HI'
    LOW = 'LO'
    MIDDLE = 'MI'
    PURCHASED = 'PU'
    PRIORITY_CHOICES = (
        (HIGH, 'High'),
        (LOW, 'Low'),
        (MIDDLE, 'Middle'),
        (PURCHASED, 'Purchased')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prospect_email = models.EmailField(max_length=100)
    prospect_phone = models.CharField(max_length=12, default=None)  # opportunity to reformat this later
    date_added = models.DateField(("Date"), auto_now_add=True)
    first_visit = models.DateField()
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    referral_source = models.CharField(max_length=50)
    multiple_visits: bool = models.BooleanField(default=False)
    #owns_property: bool = models.BooleanField(default=False)
    rent_or_own = models.CharField(max_length=1, choices=LIVING_CHOICES)
    #if owns_property:
    #home_address = models.Add
        #owns_UP: bool = models.BooleanField(default=False)
        #if not owns_UP:
            #property_location = models.CharField(max_length=200)
    buy_new_construction_only: bool = models.BooleanField(default=False)
    claims_agent: bool = models.BooleanField(default=False)
    notes = models.TextField(max_length=1000)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)

    class Meta:     #lets you define superficial things (.latest) used outside the database
        ordering = ['last_name', 'first_name', 'prospect_email', 'prospect_phone']


    def __str__(self):  #   when you print, what shows up
        return '{} {}'.format(self.first_name, self.last_name)
        #return '{} {}'.format(self.first_name, self.last_name, self.prospect_email, self.prospect_phone)


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
