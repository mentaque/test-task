import random
import string
import time

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserProfile
from app.serializers import PhoneSerializer, AuthSerializer, UserProfileSerializer, GetProfileSerializer


def generate_random_code(length=6):
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code


class EnterByPhoneView(APIView):
    @swagger_auto_schema(request_body=PhoneSerializer)
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            auth_code = str(random.randint(1000, 9999))
            user, created = UserProfile.objects.get_or_create(phone_number=phone_number, defaults={
                'auth_code': auth_code,
                'invite_code': generate_random_code(),
            })
            if not created:
                user.auth_code = auth_code
                user.is_authenticated = False
                user.save()
            time.sleep(1.5)

            return Response({'detail': f'auth code: {auth_code}'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmPhoneView(APIView):
    @swagger_auto_schema(request_body=AuthSerializer)
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            auth_code = serializer.validated_data['auth_code']
            try:
                user = UserProfile.objects.get(phone_number=phone_number)
            except:
                return Response('Invalid phone number')
            if user.auth_code != '0000' and user.auth_code == auth_code:
                user.is_authenticated = True
                user.auth_code = '0000'
                user.save()
                serializer = UserProfileSerializer(user)
                return Response({'detail': serializer.data}, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid data'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    @swagger_auto_schema(request_body=GetProfileSerializer)
    def post(self, request):
        try:
            user_profile = UserProfile.objects.get(phone_number=request.data.get('phone_number'))
        except:
            return Response('Profile does not exist')
        serializer = UserProfileSerializer(user_profile)
        invite_code = request.data.get('invite_code')
        if invite_code:
            if user_profile.is_authenticated and not user_profile.inviter and user_profile.invite_code != invite_code:
                try:
                    inviter = UserProfile.objects.get(invite_code=invite_code)
                except:
                    return Response("Invalid invite code")
                user_profile.inviter = inviter
                user_profile.save()
                return Response(serializer.data)
            return Response("You are not authenticated OR you are already enter invite code")
        return Response(serializer.data)


