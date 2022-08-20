from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id","stars","review","spoilers","recomendation","movie","user"]
        depth = 1
        

    def create(self, validated_data: dict) -> Review:

        review = Review.objects.create(**validated_data)

        return review
