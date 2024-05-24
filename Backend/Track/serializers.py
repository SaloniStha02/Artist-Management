from rest_framework import serializers
from .models import Song

class SongSerializer (serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'

    def get_artist_name(self, obj):
        return f"{obj.artist.first_name} {obj.artist.last_name}"