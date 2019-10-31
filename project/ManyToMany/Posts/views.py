from rest_framework import viewsets, mixins
from Posts import models, serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
# Create your views here.

from rest_framework.decorators import api_view, renderer_classes






class PostViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin):

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    @action(methods=['get'], detail=False,
            url_path='filterbytag', url_name='filterbytag')
    def get_FeatsByTag(self, request):
        queryset = self.queryset
        query_tag = request.query_params.get('tag', None)
        print("This is the query: " + query_tag)
        if query_tag is not None:
            queryset = queryset.filter(tags__name__icontains=query_tag)
        else:
            print("query_tag is empty")
        serializer = serializers.PostSerializer(queryset, many=True)
        return Response(serializer.data)
    