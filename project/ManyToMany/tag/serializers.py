from rest_framework import serializers

from tag import models

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(required=False, queryset=models.Tag.objects.all(), many=True)
    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'body',
            'tags',
        ]