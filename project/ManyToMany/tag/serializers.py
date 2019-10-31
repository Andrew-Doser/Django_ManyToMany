from rest_framework import serializers
from Posts import models as podels
from tag import models

class TagSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(required=False, queryset=podels.Post.objects.all(), many=True)
    class Meta:
        model = models.Tag
        fields = [
            'name',
            'posts',
        ]

