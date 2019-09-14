from django.db import models

import uuid
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
import logging
import datetime
from uuid_upload_path import upload_to
from django.utils.translation import ugettext_lazy as _

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
    first_visit_day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    referral_source = models.CharField(max_length=50)
    multiple_visits: bool = models.BooleanField(default=False)
    date_most_recent_visit = models.DateField(null=True)
    rent_or_own = models.CharField(max_length=1, choices=LIVING_CHOICES)
    buy_new_construction_only: bool = models.BooleanField(default=False)
    claims_agent: bool = models.BooleanField(default=False)
    notes = models.TextField(max_length=1000, blank=True)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    prospect_card = models.FileField(upload_to=upload_to, blank=True, null=True)
    action_item = models.CharField(blank=True, null=True, max_length=100)
    action_date = models.DateField(blank=True, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Prospect._meta.fields]

    class Meta:     #lets you define superficial things (.latest) used outside the database
        ordering = ['-date_most_recent_visit']

    def __str__(self):  #   when you print, what shows up
        return '{} {}'.format(self.first_name, self.last_name)


class Visit(TimeStampedUUIDModel):
    visit_date = models.DateField()
    visit_notes = models.CharField(max_length=100)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, related_name='visits')

    class Meta:
        ordering = ['-visit_date']
        get_latest_by = ['visit_date']

    def __str__(self):
        return '{}'.format(self.visit_date)