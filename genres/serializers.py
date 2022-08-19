from rest_framework import serializers

from .models import Genre


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=127)


    def create(self, validated_data: dict) -> Genre:
        
        genre = Genre.objects.create(**validated_data)

        return genre

