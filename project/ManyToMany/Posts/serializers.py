from rest_framework import serializers
from Posts import models as podels
from tag import models as todels

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(required=False, queryset=todels.Tag.objects.all(), many=True)
    class Meta:
        model = podels.Post
        fields = [
            'id',
            'title',
            'body',
            'tags',
        ]