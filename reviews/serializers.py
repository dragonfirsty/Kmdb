from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Review


class ReviewPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ["id","stars","review","spoilers","recomendation","movie_id","user"]
        
        
    def create(self, validated_data: dict) -> Review:

        review = Review.objects.create(**validated_data)

        return review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"
        
        

