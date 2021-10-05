from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
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
from django.db.models import Q
from wkhtmltopdf.views import PDFTemplateView
from django.conf import settings
from wkhtmltopdf.views import PDFTemplateResponse
from django.conf import settings

# Permission
class PermissionViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search = self.request.query_params.get("filter")
        if search:
            fields = [f for f in Permission._meta.fields if not isinstance(f, models.ForeignKey)]
            queries = [Q(**{f.name + '__icontains': search}) for f in fields]

            qs = Q()
            for query in queries:
                qs = qs | query

            return Permission.objects.filter(qs)
        else:
            return self.queryset

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


# ContentType
class ContentTypeViewSet(DynamicModelViewSet):
    """
    API endpoint that allows ContentTypes to be viewed or edited.
    """
    queryset = ContentType.objects.all().order_by('-id')
    serializer_class = ContentTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search = self.request.query_params.get("filter", None)

        if search:
            fields = [f for f in ContentType._meta.fields if not isinstance(f, models.ForeignKey)]
            queries = [Q(**{f.name + '__icontains': search}) for f in fields]

            qs = Q()
            for query in queries:
                qs = qs | query

            return ContentType.objects.filter(qs)
        else:
            return self.queryset
            
class ContentTypesResource(ModelResource):
    class Meta:
        model = ContentType

class ContentTypeExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows ContentTypes to be viewed or edited.
    """
    queryset = ContentType.objects.all().order_by('-id')
    serializer_class = ContentTypeSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        ContentTypes_resource = ContentTypesResource()
        dataset = ContentTypes_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="ContentTypes.xls"'
        return response


# Group
class GroupViewSet(DynamicModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search = self.request.query_params.get("filter", None)

        # fields = [f for f in Group._meta.fields if not isinstance(f, models.ForeignKey)]
        # queries = [Q(**{f.name + '__icontains': search}) for f in fields]

        # qs = Q()
        # for query in queries:
        #     qs = qs | query

        # return Group.objects.filter(qs)

        if search:
            fields = [f for f in Group._meta.fields if not isinstance(f, models.ForeignKey)]
            queries = [Q(**{f.name + '__icontains': search}) for f in fields]

            qs = Q()
            for query in queries:
                qs = qs | query

            return Group.objects.filter(qs)

        else:
            return self.queryset


class GroupsResource(ModelResource):
    class Meta:
        model = Group

class GroupExportViewSet(DynamicModelViewSet):
    """
    API endpoint that allows permission to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        permission_resource = GroupsResource()
        dataset = permission_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="group.xls"'
        return response

# User
class UserViewSet(DynamicModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search = self.request.query_params.get("filter", None)

        if search:
            fields = [f for f in User._meta.fields if not isinstance(f, models.ForeignKey)]
            queries = [Q(**{f.name + '__icontains': search}) for f in fields]

            qs = Q()
            for query in queries:
                qs = qs | query

            return User.objects.filter(qs)
        else:
            return self.queryset
            
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

