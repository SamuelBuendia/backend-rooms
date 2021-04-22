from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from django.contrib.auth.models import Group, User, Permission
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import *

from simple_history.admin import SimpleHistoryAdmin

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

## Permission
class PermissionsResource(ModelResource):
    class Meta:
        model = Permission

@admin.register(Permission)
class PermissionAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = PermissionsResource

## User
admin.site.unregister(User)
class UsersResource(ModelResource):
    class Meta:
        model = User

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    search_fields = ('username',)
    ordering = ('id',)
    resource_class = UsersResource

## Group
admin.site.unregister(Group)
class GroupsResource(ModelResource):
    class Meta:
        model = Group

@admin.register(Group)
class GroupAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = GroupsResource

## Session
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    search_fields = ('session_key',)
    ordering = ('session_key',)

## LogEntry
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    search_fields = ('user_id',)
    ordering = ('user_id',)

## UserProfile
class UserProfilesResource(ModelResource):
    class Meta:
        model = UserProfile

class UserProfileAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = UserProfilesResource

admin.site.register(UserProfile, UserProfileAdmin)

## Functionary
class FunctionarysResource(ModelResource):
    class Meta:
        model = Functionary

class FunctionaryAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = FunctionarysResource

admin.site.register(Functionary, FunctionaryAdmin)
