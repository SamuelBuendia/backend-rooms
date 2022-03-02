from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from django.utils.translation import gettext_lazy as _

from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

## UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.user

## Functionary
class Functionary(SafeDeleteModel):
    name = models.CharField(max_length=255, unique=False)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    identification_number = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    institutional_email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    personal_email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    birth_date = models.DateField(null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='functionary')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('functionary')
        verbose_name_plural = _('functionarys')
        ordering = ['-id']

    def __str__(self):
        return self.name

## Space
class Space(SafeDeleteModel):
    name = models.CharField(max_length=255)
    number_space = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    functionary = models.ForeignKey(Functionary, on_delete=models.CASCADE, null=True, blank=True, related_name='functionaryspace')
    functionarys = models.ManyToManyField(Functionary, related_name='spacefunctionarys')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('space')
        verbose_name_plural = _('spaces')
        ordering = ['-id']

    def __str__(self):
        return self.name

## Room
class Room(SafeDeleteModel):
    name = models.CharField(max_length=255)
    number_room = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    functionary = models.ForeignKey(Functionary, on_delete=models.CASCADE, null=True, blank=True, related_name='functionaryroom')
    space = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, blank=True, related_name='spaceroom')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
        ordering = ['-id']

    def __str__(self):
        return self.name


## Folder
class Folder(SafeDeleteModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    expiration_date = models.DateField(null=True)
    guide_file = models.FileField(db_column='file_url', blank=True, null=True, upload_to='GuideFile/')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    functionary = models.ForeignKey(Functionary, on_delete=models.CASCADE, null=True, blank=True, related_name='functionaryfolder')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='folderroom')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('folder')
        verbose_name_plural = _('folders')
        ordering = ['-id']

    def __str__(self):
        return self.name