from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:

        genres_data = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for value in genres_data:
            genre, _ = Genre.objects.get_or_create(**value)
            movie.genres.add(genre)

        return movie

    def update(self,instance: Movie,validated_data: dict,)-> Movie:
        
        if 'genres' in validated_data:
            genres_data = validated_data.pop("genres")
            if len(genres_data) > 0:
                instance.genres.set([]) 
                for value in genres_data:
                    genre, _ = Genre.objects.get_or_create(**value)
                    instance.genres.add(genre)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance    

      