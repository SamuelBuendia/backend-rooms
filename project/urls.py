"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project.api import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from dynamic_rest.routers import DynamicRouter
from django.conf import settings
from django.conf.urls.static import static

router = DynamicRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contenttypes', views.ContentTypeViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'usersprofile', views.UserProfileViewSet)
router.register(r'functionarys', views.FunctionaryViewSet, base_name='Functionarys')
router.register(r'spaces', views.SpaceViewSet, base_name='Spaces')
router.register(r'rooms', views.RoomViewSet, base_name='Rooms')
router.register(r'folders', views.FolderViewSet, base_name='Folders')
router.register(r'evidences', views.EvidenceViewSet, base_name='Evidences')

router.register(r'export/users', views.UserExportViewSet, base_name='Exportusers'),
router.register(r'export/contenttypes', views.ContentTypeExportViewSet, base_name='ExportContentTypes'),
router.register(r'export/permissions', views.PermissionExportViewSet, base_name='ExportPermissions'),
router.register(r'export/functionarys', views.FunctionaryExportViewSet, base_name='ExportFunctionarys'),
router.register(r'export/spaces', views.SpaceExportViewSet, base_name='ExportSpaces'),
router.register(r'export/rooms', views.RoomExportViewSet, base_name='ExportRooms'),
router.register(r'export/folders', views.FolderExportViewSet, base_name='ExportFolders'),
router.register(r'export/evidences', views.EvidenceExportViewSet, base_name='ExportEvidences'),

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/pdf/guides', views.GuidePDFViewSet.as_view()),
    path('api/v1/auth', include('djoser.urls.authtoken')),
    path('api/v1/auth/user', views.AuthTokenUserViewSet.as_view()),
    path('api/v1/auth/token', views.AuthTokenViewSet.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)