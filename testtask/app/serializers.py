from django.core.validators import RegexValidator
from rest_framework import serializers

from app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    inviter = serializers.StringRelatedField()
    invited_people = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        exclude = ('auth_code',)

    def get_invited_people(self, obj):
        invited_people = UserProfile.objects.filter(inviter=obj)
        invited_people_numbers = [user.phone_number for user in invited_people]
        return invited_people_numbers


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number']


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'auth_code']


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'invite_code']