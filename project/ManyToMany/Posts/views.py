from rest_framework import viewsets, mixins
from Posts import models, serializers
from django.http import HttpResponse
from rest_framework.decorators import action
# Create your views here.


def retrieve(request):
    queryset = models.Post.objects.all()
    query_tag = request.GET.get('tag', None)
    print(query_tag)
    if query_tag is not None:
        queryset = queryset.filter(tags__name__icontains=query_tag)
    else:
        print("query_tag is empty")
    return HttpResponse(queryset)



class PostViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin):

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


    