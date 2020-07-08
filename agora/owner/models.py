from __future__ import unicode_literals
import uuid
from django.db import models
from accounts.models import Organisation

class ContactInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, default=None, blank=False, null=True)
    last_name = models.CharField(max_length=50, default=None, blank=False,  null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, default=None, blank=True, null=True)
    position = models.CharField(max_length=50, default=None, blank=True, null=True)
    organisation = models.ForeignKey(Organisation,   related_name="contacts")
