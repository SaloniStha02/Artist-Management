from django.shortcuts import render
from .models import Song
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SongSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.shortcuts import get_object_or_404


class IsArtistOrAdmin(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_artist or (request.user.is_superuser and request.user.is_staff))
    

class SongList(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        songs = Song.objects.filter(is_deleted=False)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_artist:
                serializer.save(artist=request.user)  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Only artists can create songs."}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetailList(APIView):
    permission_classes = [IsAuthenticated, IsArtistOrAdmin]  

    def get_object(self, pk):
        return get_object_or_404(Song, pk=pk)

    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            if request.user == song.artist or request.user.is_superuser:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"error": "No permission to update this song."}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            if request.user == song.artist or request.user.is_superuser:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"error": "No permission to update this song."}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        song = self.get_object(pk)
        if request.user == song.artist or request.user.is_superuser:
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No permission to delete this song."}, status=status.HTTP_403_FORBIDDEN)





