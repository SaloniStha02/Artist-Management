from django.shortcuts import render
from .models import NewUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import UserSerializer
from .manager import UserManager
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

class IsStaffOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff and request.user.is_superuser:
            return True
        return obj == request.user
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=NewUser.objects.filter(is_deleted=False)
        serializer=UserSerializer(user, many=True)
        return Response(serializer.data)

class UserRegister(APIView):
 
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_type = request.data.get('user_type', 'regular')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            other_fields = {k: v for k, v in serializer.validated_data.items() if k not in ['email', 'password']}
            
            if user_type == 'admin':
                user = NewUser.objects.create_superuser(email=email, password=password, **other_fields)
            elif user_type == 'artist':
                user = NewUser.objects.create_artist(email=email, password=password, **other_fields)
            else:
                user = NewUser.objects.create_user(email=email, password=password, **other_fields)
                
            response_data = serializer.data
            response_data['user_type'] = user_type
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise 

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        users = self.get_object(pk)
        self.check_object_permissions(request, users)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data.get('password', user.password))
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
     
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        user_type = 'regular'
        if user.is_superuser:
            user_type = 'admin'
        elif user.is_artist:
            user_type = 'artist'

        data = {
            'access': response.data['access'],
            'refresh': response.data['refresh'],
            'user_type': user_type,
            'user_id': user.id,
            'user_email': user.email
        }
        print(data)
        return Response(data)
    
class ArtistView(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request):
        users = NewUser.objects.filter(is_artist=True,is_deleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class AdminView(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request):
        users = NewUser.objects.filter(is_superuser=True ,is_staff=True,is_deleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    


class NormalUserList(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request):
        users = NewUser.objects.filter(is_superuser=False ,is_staff=False, is_artist=False,is_deleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
