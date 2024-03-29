"""
Creates api endpoints for Crud operations
"""

from rest_framework import viewsets, mixins
from tag import models, serializers
# Create your views here.




class TagViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
    ):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer