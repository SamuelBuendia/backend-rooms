from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from django.utils.translation import gettext_lazy as _

from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

## UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(upload_to='profile_image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

## Employee
class Employee(SafeDeleteModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='employee')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        ordering = ['-id']

    def __str__(self):
        return self.name