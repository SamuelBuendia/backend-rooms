from django.contrib.auth.models import User, Group, Permission
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework.relations import HyperlinkedIdentityField
from dynamic_rest.fields.fields import DynamicRelationField
from .models import *
from django.contrib.auth.hashers import make_password

## Permission
class PermissionSerializer(DynamicModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

## Group
class GroupSerializer(DynamicModelSerializer):
    permissions = DynamicRelationField('PermissionSerializer', many=True)
    class Meta:
        model = Group
        fields = "__all__"

## UserProfile
class UserProfileSerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer', many=False)
    class Meta:
        model = UserProfile
        fields = '__all__'

## User
class UserSerializer(DynamicModelSerializer):
    userprofile = DynamicRelationField('UserProfileSerializer', many=False)
    groups = DynamicRelationField('GroupSerializer', many=True)
    user_permissions = DynamicRelationField('PermissionSerializer', many=True)
    functionary = DynamicRelationField('FunctionarySerializer', many=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        if (validated_data.get('password') != instance.password):
            validated_data['password'] = make_password(validated_data.get('password'))
        else:
            validated_data.pop('password')

        validated_data.pop('groups')
        validated_data.pop('user_permissions')
        validated_data.pop('functionary')
        validated_data.pop('userprofile')
        user = super().update(instance, validated_data)
        return user

## AuthToken
class AuthTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refreshToken'] = str(refresh)
        data['accessToken'] = str(refresh.access_token)
        del data['access']
        del data['refresh']
        return data

## Functionary
class FunctionarySerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer', many=False)
    class Meta:
        model = Functionary
        fields = '__all__'

## Room
class RoomSerializer(DynamicModelSerializer):
    functionary = DynamicRelationField('FunctionarySerializer', many=False)
    room_fk = DynamicRelationField('RoomSerializer', many=False)
    class Meta:
        model = Room
        fields = '__all__'
