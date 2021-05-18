from django.contrib.auth.models import User, Group, Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from project.api.serializer import UserSerializer, GroupSerializer, AuthTokenSerializer, PermissionSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from dynamic_rest.viewsets import DynamicModelViewSet
from django.http import HttpResponse
from import_export.resources import ModelResource
from .models import *
from .serializer import *
from wkhtmltopdf.views import PDFTemplateView
from django.conf import settings
from wkhtmltopdf.views import PDFTemplateResponse
from django.conf import settings

class PermissionViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(DynamicModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(DynamicModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UsersResource(ModelResource):
    class Meta:
        model = User

class UserExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        users_resource = UsersResource()
        dataset = users_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'
        return response

class PermissionsResource(ModelResource):
    class Meta:
        model = Permission

class PermissionExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permission to be viewed or edited.
    """
    queryset = Permission.objects.all().order_by('-id')
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        permission_resource = PermissionsResource()
        dataset = permission_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="permission.xls"'
        return response

class UserProfileViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    UserProfile_classes = [IsAuthenticated]
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated]

class AuthTokenViewSet(TokenObtainPairView):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    serializer_class = AuthTokenSerializer

class AuthTokenUserViewSet(APIView):
    """
    API endpoint that return auth user.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'userprofile'
    def get(self, request):
        """
        Return the auth user.
        """
        return Response(UserSerializer(request.user, context={'request': request}).data)

## Functionary
class FunctionaryViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Functionary.objects.all()
    serializer_class = FunctionarySerializer
    Functionary_classes = [IsAuthenticated]
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated]

class FunctionaryResource(ModelResource):
    class Meta:
        model = Functionary

class FunctionaryExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Functionary.objects.all().order_by('-id')
    serializer_class = FunctionarySerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        resource = FunctionaryResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="functionarys.xls"'
        return response

## Space
class SpaceViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    Space_classes = [IsAuthenticated]
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated]

class SpaceResource(ModelResource):
    class Meta:
        model = Space

class SpaceExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Space.objects.all().order_by('-id')
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        resource = SpaceResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="space.xls"'
        return response

## Room
class RoomViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    Room_classes = [IsAuthenticated]
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated]

class RoomResource(ModelResource):
    class Meta:
        model = Room

class RoomExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        resource = RoomResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="rooms.xls"'
        return response

