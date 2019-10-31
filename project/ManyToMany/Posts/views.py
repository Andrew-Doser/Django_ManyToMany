from rest_framework import viewsets, mixins
from Posts import models, serializers
from rest_framework.decorators import action
# Create your views here.
class PostViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin):

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    @action(detail=False, methods=['get'])
    def getPostsByTag(self, request):
        queryset = self.queryset
        query_tag = request.query_params.get('tag', None)
        if query_tag is not None:
            queryset = queryset.filter(tags__name__icontains=query_tag)
        return queryset